"""
Main Agent Class
Handles task execution and orchestration
"""

import logging
import time
from datetime import datetime
from typing import Dict, List, Any, Optional
from .tool_registry import ToolRegistry


class Agent:
    """Main AI Agent class for task automation"""
    
    def __init__(self, name: str = "CodevAgent"):
        """
        Initialize the agent
        
        Args:
            name: Name of the agent
        """
        self.name = name
        self.tool_registry = ToolRegistry()
        self.task_history: List[Dict[str, Any]] = []
        self.logger = self._setup_logger()
        
    def _setup_logger(self) -> logging.Logger:
        """Setup logging configuration"""
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.INFO)
        
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        ch.setFormatter(formatter)
        
        if not logger.handlers:
            logger.addHandler(ch)
        
        return logger
    
    def execute_task(self, task: str, tool_name: Optional[str] = None) -> Dict[str, Any]:
        """
        Execute a task using available tools
        
        Args:
            task: Task description
            tool_name: Specific tool to use (optional)
        
        Returns:
            Dictionary with execution results
        """
        start_time = time.time()
        task_id = len(self.task_history) + 1
        
        self.logger.info(f"Starting task {task_id}: {task}")
        
        result = {
            "task_id": task_id,
            "task": task,
            "status": "pending",
            "result": None,
            "error": None,
            "tool_used": None,
            "start_time": datetime.now().isoformat(),
            "duration": 0
        }
        
        try:
            # Select appropriate tool
            if tool_name:
                if not self.tool_registry.has_tool(tool_name):
                    raise ValueError(f"Tool '{tool_name}' not found")
                tool = self.tool_registry.get_tool(tool_name)
            else:
                # Auto-select tool based on task keywords
                tool_name = self._select_tool(task)
                tool = self.tool_registry.get_tool(tool_name)
            
            self.logger.info(f"Using tool: {tool_name}")
            result["tool_used"] = tool_name
            
            # Execute the tool
            tool_result = tool.execute(task)
            
            result["status"] = "completed"
            result["result"] = tool_result
            
            self.logger.info(f"Task {task_id} completed successfully")
            
        except Exception as e:
            result["status"] = "failed"
            result["error"] = str(e)
            self.logger.error(f"Task {task_id} failed: {str(e)}")
        
        # Calculate duration
        result["duration"] = time.time() - start_time
        result["end_time"] = datetime.now().isoformat()
        
        # Store in history
        self.task_history.append(result)
        
        return result
    
    def _select_tool(self, task: str) -> str:
        """
        Select appropriate tool based on task keywords
        
        Args:
            task: Task description
        
        Returns:
            Tool name
        """
        task_lower = task.lower()
        
        # Simple keyword-based selection
        if any(keyword in task_lower for keyword in ["search", "find", "lookup", "query"]):
            return "search"
        elif any(keyword in task_lower for keyword in ["code", "generate", "create", "implement", "write"]):
            return "code_generator"
        elif any(keyword in task_lower for keyword in ["document", "doc", "explain", "describe", "define"]):
            return "docs"
        else:
            # Default to search
            return "search"
    
    def get_task_history(self) -> List[Dict[str, Any]]:
        """Get all task execution history"""
        return self.task_history
    
    def get_task_by_id(self, task_id: int) -> Optional[Dict[str, Any]]:
        """Get specific task by ID"""
        for task in self.task_history:
            if task["task_id"] == task_id:
                return task
        return None
    
    def list_tools(self) -> List[str]:
        """List all available tools"""
        return self.tool_registry.list_tools()
    
    def get_tool_info(self, tool_name: str) -> Dict[str, Any]:
        """Get information about a specific tool"""
        tool = self.tool_registry.get_tool(tool_name)
        return {
            "name": tool.name,
            "description": tool.description,
            "version": getattr(tool, "version", "1.0.0")
        }
