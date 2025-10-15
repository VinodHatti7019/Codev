"""Codev Agent - Main Agent Class

Vinod-powered AI Agent for task execution and automation.
"""

import logging
from typing import Dict, Any, List, Optional
from tool_registry import ToolRegistry

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CodevAgent:
    """Main agent class for task orchestration and execution."""
    
    def __init__(self, name: str = "Codev"):
        self.name = name
        self.tool_registry = ToolRegistry()
        self.task_history: List[Dict[str, Any]] = []
        logger.info(f"Initialized {self.name} agent")
    
    def register_tool(self, tool_name: str, tool_func, description: str):
        """Register a new tool with the agent."""
        self.tool_registry.register(tool_name, tool_func, description)
        logger.info(f"Registered tool: {tool_name}")
    
    def execute_task(self, task_name: str, **kwargs) -> Dict[str, Any]:
        """Execute a registered task/tool."""
        try:
            logger.info(f"Executing task: {task_name}")
            result = self.tool_registry.execute(task_name, **kwargs)
            
            # Record task execution
            task_record = {
                'task': task_name,
                'status': 'success',
                'result': result,
                'params': kwargs
            }
            self.task_history.append(task_record)
            
            return task_record
        except Exception as e:
            logger.error(f"Task execution failed: {e}")
            task_record = {
                'task': task_name,
                'status': 'failed',
                'error': str(e),
                'params': kwargs
            }
            self.task_history.append(task_record)
            return task_record
    
    def list_tools(self) -> List[str]:
        """List all registered tools."""
        return self.tool_registry.list_tools()
    
    def get_task_history(self) -> List[Dict[str, Any]]:
        """Get agent's task execution history."""
        return self.task_history
    
    def clear_history(self):
        """Clear task execution history."""
        self.task_history = []
        logger.info("Task history cleared")


if __name__ == "__main__":
    # Example usage
    agent = CodevAgent()
    print(f"Agent '{agent.name}' initialized successfully!")
    print(f"Available tools: {agent.list_tools()}")
