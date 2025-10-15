"""
Tool Registry
Manages and provides access to all available tools
"""

from typing import Dict, List
from .tools import BaseTool, SearchTool, CodeGeneratorTool, DocsTool


class ToolRegistry:
    """Registry for managing agent tools"""
    
    def __init__(self):
        """Initialize tool registry with default tools"""
        self.tools: Dict[str, BaseTool] = {}
        self._register_default_tools()
    
    def _register_default_tools(self):
        """Register default tools"""
        self.register_tool(SearchTool())
        self.register_tool(CodeGeneratorTool())
        self.register_tool(DocsTool())
    
    def register_tool(self, tool: BaseTool):
        """
        Register a new tool
        
        Args:
            tool: Tool instance to register
        """
        self.tools[tool.name] = tool
    
    def get_tool(self, name: str) -> BaseTool:
        """
        Get tool by name
        
        Args:
            name: Tool name
        
        Returns:
            Tool instance
        
        Raises:
            KeyError: If tool not found
        """
        if name not in self.tools:
            raise KeyError(f"Tool '{name}' not found")
        return self.tools[name]
    
    def has_tool(self, name: str) -> bool:
        """
        Check if tool exists
        
        Args:
            name: Tool name
        
        Returns:
            True if tool exists, False otherwise
        """
        return name in self.tools
    
    def list_tools(self) -> List[str]:
        """
        List all registered tools
        
        Returns:
            List of tool names
        """
        return list(self.tools.keys())
    
    def get_all_tools(self) -> Dict[str, BaseTool]:
        """
        Get all registered tools
        
        Returns:
            Dictionary of all tools
        """
        return self.tools.copy()
