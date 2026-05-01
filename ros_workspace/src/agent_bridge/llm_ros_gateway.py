# File: ros_workspace/src/agent_bridge/llm_ros_gateway.py
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
from fastapi import FastAPI
import uvicorn
import threading

app = FastAPI()
node = None

class AgentGatewayNode(Node):
    def __init__(self):
        super().__init__('llm_ros_gateway')
        self.current_x = 0.0
        self.current_y = 0.0
        self.current_z = 0.0
        
        # 订阅 VINS-Fusion 里程计
        self.odom_sub = self.create_subscription(
            Odometry,
            '/vins_estimator/odometry',
            self.odom_callback,
            10
        )
        
        # 发布给 EGO-Planner 的目标点
        self.goal_pub = self.create_publisher(
            PoseStamped,
            '/move_base_simple/goal', # 假设EGO接收的话题
            10
        )
        
    def odom_callback(self, msg):
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y
        self.current_z = msg.pose.pose.position.z

    def send_goal(self, x, y, z):
        goal_msg = PoseStamped()
        goal_msg.header.stamp = self.get_clock().now().to_msg()
        goal_msg.header.frame_id = "world"
        goal_msg.pose.position.x = float(x)
        goal_msg.pose.position.y = float(y)
        goal_msg.pose.position.z = float(z)
        goal_msg.pose.orientation.w = 1.0 # 保持默认朝向
        self.goal_pub.publish(goal_msg)
        return True

@app.get("/uav/status")
def get_status():
    if node:
        return {"status": "ok", "position": {"x": node.current_x, "y": node.current_y, "z": node.current_z}}
    return {"status": "error", "message": "ROS Node not initialized"}

@app.post("/uav/goal")
def set_goal(x: float, y: float, z: float):
    if node:
        node.send_goal(x, y, z)
        return {"status": "success", "message": f"Goal set to {x}, {y}, {z}"}
    return {"status": "error"}

def ros_spin_thread():
    rclpy.init()
    global node
    node = AgentGatewayNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    # 在独立线程中运行 ROS 节点
    threading.Thread(target=ros_spin_thread, daemon=True).start()
    # 启动 HTTP API 网关
    uvicorn.run(app, host="0.0.0.0", port=8000)
