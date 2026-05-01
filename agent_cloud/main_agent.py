# File: agent_cloud/main_agent.py
import asyncio
import os
import json
from openai import AsyncOpenAI
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession

# 兼容 Xiaomi MiMo V2.5 API 或标准 OpenAI
client = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", "your-api-key"),
    base_url=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
)
MODEL_NAME = "gpt-4o" # 或 mimo-v2.5

SYSTEM_PROMPT = """你是一个具身智能控制系统的大脑。
你有三个工具：get_uav_status, set_navigation_goal, execute_robot_expression。
请监控状态，并在需要时自主探索环境（设置航点）或进行交互（改变表情）。
不要每次都调用动作，如果没有特殊情况，只观察即可。"""

async def agentic_loop():
    # 配置连接到本地运行的 MCP Server
    server_params = StdioServerParameters(
        command="python3",
        args=["../mcp_server/server.py"]
    )
    
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            print("[Agent] MCP Session initialized. Starting control loop...")
            
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            token_usage_total = 0
            
            while True:
                # 获取可用工具
                tools_response = await session.list_tools()
                tools_schema = [{
                    "type": "function",
                    "function": {
                        "name": tool.name,
                        "description": tool.description,
                        "parameters": tool.inputSchema
                    }
                } for tool in tools_response.tools]

                # 驱动大模型进行决策
                response = await client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=messages,
                    tools=tools_schema,
                    tool_choice="auto",
                    temperature=0.3
                )
                
                msg = response.choices[0].message
                token_usage_total += response.usage.total_tokens
                print(f"[Tokens] Current Loop: {response.usage.total_tokens} | Total: {token_usage_total}")

                if msg.tool_calls:
                    for tool_call in msg.tool_calls:
                        func_name = tool_call.function.name
                        args = json.loads(tool_call.function.arguments)
                        print(f"[Agent -> MCP] Calling Tool: {func_name}({args})")
                        
                        # 动态调用 MCP Server 上的 Tool
                        result = await session.call_tool(func_name, arguments=args)
                        result_text = result.content[0].text if result.content else "OK"
                        
                        messages.append(msg) # 加入模型的 function call
                        messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": result_text
                        })
                else:
                    # 常规待机日志
                    print(f"[Agent Log] 待机状态: {msg.content}")
                    # 防止上下文无限膨胀，仅保留最近N轮对话
                    if len(messages) > 10:
                        messages = [messages[0]] + messages[-5:]
                
                # 保持 5 秒的控制循环频率
                await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(agentic_loop())
