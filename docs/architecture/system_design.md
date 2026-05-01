# Enterprise System Design

## 1. Introduction
This document outlines the architecture for the Enterprise Embodied AI Multi-Agent System. The system is designed for high availability, fault tolerance, and secure execution of Agentic workflows bridging cloud LLMs and physical robots via Model Context Protocol (MCP).

## 2. Component Architecture
- **Agent Cloud (Kubernetes Deployment)**: Horizontally scaled pods running the Agentic loop. Interacts with OpenAI/Local LLMs. Uses Weaviate Vector DB for long-term spatial and episodic memory.
- **MCP Server (Middleware Layer)**: Acts as the secure boundary. Implements JWT/RBAC auth to prevent unauthorized actuation commands to the hardware. Rate-limited at 100 QPS.
- **ROS 2 Gateway (DDS Network)**: Interfaces with Real-Time processes. Consumes `/vins_estimator/odometry` and translates semantic commands into continuous trajectory goals.
- **STM32 Hardware Layer**: Raw C/C++ running on FreeRTOS or Bare-metal (Cortex-M4). 

## 3. Data Flow
1. Telemetry -> ROS2 -> HTTP GET -> MCP Server -> Agent Cloud
2. Agent Reasoning (Context + Vector DB + Prompt)
3. Action Decision -> MCP Tool Call -> HTTP POST -> ROS2 / Serial -> Hardware

## 4. Security
- Secrets managed via K8s Secret Ref.
- All intra-service communication within K8s is encrypted via Istio mTLS.
- Hardware node disconnected from external internet; strictly airgapped behind the ROS gateway.
