"""Tool Registry System

Manages agent tools/plugins and task execution.
"""

import logging
from typing import Dict, Callable, Any

logger = logging.getLogger(__name__)


class ToolRegistry:
    """Registry system for agent plugins and tasks."""
    
    def __init__(self):
        self.tools: Dict[str, Dict[str, Any]] = {}
        logger.info("ToolRegistry initialized")
        self._register_default_tools()
    
    def _register_default_tools(self):
        """Register default tools/tasks."""
        # Hello World task
        def hello_world(name: str = "World") -> str:
            return f"Hello, {name}! Welcome to Codev agent system."
        
        # Echo task
        def echo(message: str) -> str:
            return f"Echo: {message}"
        
        # Calculator task
        def calculate(operation: str, a: float, b: float) -> float:
            ops = {
                'add': lambda x, y: x + y,
                'subtract': lambda x, y: x - y,
                'multiply': lambda x, y: x * y,
                'divide': lambda x, y: x / y if y != 0 else None
            }
            if operation in ops:
                return ops[operation](a, b)
            raise ValueError(f"Unknown operation: {operation}")
        
        # Register default tasks
        self.register('hello_world', hello_world, 'Greet a user')
        self.register('echo', echo, 'Echo a message')
        self.register('calculate', calculate, 'Perform basic calculations')
    
    def register(self, name: str, func: Callable, description: str):
        """Register a new tool."""
        self.tools[name] = {
            'func': func,
            'description': description
        }
        logger.info(f"Registered tool: {name}")
    
    def execute(self, tool_name: str, **kwargs) -> Any:
        """Execute a registered tool."""
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' not found")
        
        tool = self.tools[tool_name]
        return tool['func'](**kwargs)
    
    def list_tools(self) -> list:
        """List all registered tools."""
        return [
            {'name': name, 'description': info['description']}
            for name, info in self.tools.items()
        ]
    
    def get_tool_info(self, tool_name: str) -> Dict[str, Any]:
        """Get information about a specific tool."""
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' not found")
        return {
            'name': tool_name,
            'description': self.tools[tool_name]['description']
        }


if __name__ == "__main__":
    # Example usage
    registry = ToolRegistry()
    print("Available tools:")
    for tool in registry.list_tools():
        print(f"  - {tool['name']}: {tool['description']}")
    
    # Test hello_world
    result = registry.execute('hello_world', name='Agent')
    print(f"\n{result}")
