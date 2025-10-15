"""
Base Tool Class
Abstract base class for all tools
"""

from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """Abstract base class for all agent tools"""
    
    def __init__(self, name: str, description: str):
        """
        Initialize base tool
        
        Args:
            name: Tool name
            description: Tool description
        """
        self.name = name
        self.description = description
        self.version = "1.0.0"
    
    @abstractmethod
    def execute(self, task: str) -> Any:
        """
        Execute the tool with given task
        
        Args:
            task: Task description
        
        Returns:
            Tool execution result
        """
        pass
    
    def validate_input(self, task: str) -> bool:
        """
        Validate input task
        
        Args:
            task: Task description
        
        Returns:
            True if valid, False otherwise
        """
        return task is not None and len(task.strip()) > 0
