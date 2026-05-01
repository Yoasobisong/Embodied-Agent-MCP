# Embodied-Agent-MCP (Enterprise Edition)

![Build Status](https://github.com/enterprise/embodied-agent-mcp/actions/workflows/ci.yml/badge.svg)
![Version](https://img.shields.io/badge/version-2.5.0-blue)
![License](https://img.shields.io/badge/license-Proprietary-red)

企业级分布式的具身智能多智能体协同架构，基于 Model Context Protocol (MCP) 与 Kubernetes 构建。

## 系统特性
- **高可用架构**: 支持 Kubernetes 弹性扩缩容，包含健康探针与 Istio mTLS 接入。
- **微服务编排**: 提供完整的 `docker-compose.yml` 用于本地验证，涵盖 Redis, Weaviate (向量数据库), ROS 网关以及大模型主循环。
- **长期记忆 (Vector DB)**: Agent 具备事件记忆 (Episodic Memory) 和空间场景图记忆，由 Weaviate 强力驱动。
- **RBAC 鉴权拦截**: MCP Server 搭载中间件，硬件控制接口强制执行 JWT 基于角色的访问控制，确保机械臂/无人机不被越权操控。
- **工业级 CI/CD**: 完善的 GitHub Actions 流水线，覆盖 Python Linter (Black/Flake8), MyPy 静态类型检查，以及 STM32 固件的交叉编译。
- **裸机嵌入式 (Bare-metal)**: STM32G431 固件支持高速串口解析与 26 自由度多路 PWM 精确插值输出。

## 目录结构
```text
Embodied-Agent-MCP/
├── agent_cloud/          # 云端核心智能体层 (Asyncio, LLM)
│   ├── memory/           # 向量数据库驱动的长期记忆模块
│   ├── skills/           # Agent 可加载的技能库 (RAG 检索目标)
│   └── main_agent.py     
├── mcp_server/           # MCP 通信中间件与服务暴露
│   ├── middleware/       # 身份认证与频率限制网关
│   └── server.py
├── ros_workspace/        # ROS 2 桥接节点 (FastAPI + RCLPY)
│   ├── src/agent_bridge/ # 核心 Package (包含 package.xml, CMakeLists等)
├── stm32_firmware/       # 硬件执行固件
│   ├── Core/             # HAL 库自动生成的代码核心
│   ├── Drivers/          # 芯片驱动抽象层
│   ├── Makefile          # ARM GCC 编译配置
│   └── main.c
├── docker-compose.yml    # 本地一键微服务启动
├── k8s/                  # Kubernetes 生产环境部署清单
├── .github/workflows/    # CI/CD 自动化流水线
└── docs/                 # 系统架构白皮书与 API 文档
```

## 快速启动 (Development)
```bash
docker-compose up --build -d
```
> 注：生产环境部署请参考 `k8s/deployments/` 目录下的清单文件使用 `kubectl apply -f`。
