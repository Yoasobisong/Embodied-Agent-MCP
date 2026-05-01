# File: mcp_server/server.py
import requests
import serial
from mcp.server.fastmcp import FastMCP

# 配置参数
ROS_GATEWAY_URL = "http://localhost:8000"
SERIAL_PORT = "/dev/ttyUSB0"
BAUD_RATE = 115200

# 初始化 FastMCP 服务器
mcp = FastMCP("Embodied-Agent-Hardware-Abstractions")

try:
    stm32_serial = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
except Exception as e:
    print(f"Warning: Serial port not available: {e}")
    stm32_serial = None

@mcp.tool()
def get_uav_status() -> str:
    """获取无人机当前的 VINS-Fusion 位置与状态"""
    try:
        response = requests.get(f"{ROS_GATEWAY_URL}/uav/status")
        return response.text
    except Exception as e:
        return f'{{"status": "error", "message": "{str(e)}"}}'

@mcp.tool()
def set_navigation_goal(x: float, y: float, z: float) -> str:
    """向 ROS 网关下发新航点，供 EGO-Planner 规划轨迹"""
    try:
        response = requests.post(f"{ROS_GATEWAY_URL}/uav/goal", params={"x": x, "y": y, "z": z})
        return response.text
    except Exception as e:
        return f'{{"status": "error", "message": "{str(e)}"}}'

@mcp.tool()
def execute_robot_expression(expression_id: int) -> str:
    """通过串口向 STM32 发送指令，驱动 26 自由度舵机执行特定表情。参数为表情ID。"""
    if stm32_serial and stm32_serial.is_open:
        command = f'{{"exp": {expression_id}}}\n'
        stm32_serial.write(command.encode('utf-8'))
        return f'{{"status": "success", "expression": {expression_id}}}'
    return '{"status": "error", "message": "Serial connection closed or invalid"}'

if __name__ == "__main__":
    # 使用 stdio 传输机制运行 MCP Server，供云端 Agent 客户端调用
    mcp.run()
