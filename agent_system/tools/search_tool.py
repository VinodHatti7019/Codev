"""
Search Tool
Simulates search functionality with mock data
"""

import random
from typing import Dict, List, Any
from .base_tool import BaseTool


class SearchTool(BaseTool):
    """Tool for searching information"""
    
    def __init__(self):
        super().__init__(
            name="search",
            description="Search for information across various sources"
        )
        self.mock_results = [
            "Python is a high-level programming language known for its simplicity and readability.",
            "Machine Learning is a subset of AI that enables systems to learn from data.",
            "Flask is a lightweight WSGI web application framework in Python.",
            "Docker is a platform for developing, shipping, and running applications in containers.",
            "Git is a distributed version control system for tracking changes in source code.",
            "REST API is an architectural style for designing networked applications.",
            "Neural Networks are computing systems inspired by biological neural networks.",
            "Cloud Computing provides on-demand computing resources over the internet.",
            "Kubernetes is an open-source container orchestration platform.",
            "DevOps combines software development and IT operations for faster delivery."
        ]
    
    def execute(self, task: str) -> Dict[str, Any]:
        """
        Execute search based on task
        
        Args:
            task: Search query
        
        Returns:
            Search results
        """
        if not self.validate_input(task):
            raise ValueError("Invalid search query")
        
        # Simulate search by returning relevant mock results
        num_results = random.randint(2, 5)
        results = random.sample(self.mock_results, min(num_results, len(self.mock_results)))
        
        return {
            "query": task,
            "num_results": len(results),
            "results": results,
            "source": "Mock Search Engine"
        }
