"""
Documentation Tool
Provides documentation and explanations
"""

from typing import Dict, Any
from .base_tool import BaseTool


class DocsTool(BaseTool):
    """Tool for generating documentation and explanations"""
    
    def __init__(self):
        super().__init__(
            name="docs",
            description="Generate documentation and explanations"
        )
        self.knowledge_base = {
            "python": "Python is a high-level, interpreted programming language with dynamic semantics. It supports multiple programming paradigms including procedural, object-oriented, and functional programming.",
            "flask": "Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or other components.",
            "api": "API (Application Programming Interface) is a set of protocols, routines, and tools for building software applications. It specifies how software components should interact.",
            "rest": "REST (Representational State Transfer) is an architectural style for designing networked applications. It relies on stateless, client-server communication protocol, almost always HTTP.",
            "docker": "Docker is a platform for developers to develop, deploy, and run applications with containers. Containers package code and all dependencies so the application runs quickly and reliably.",
            "machine learning": "Machine Learning is a method of data analysis that automates analytical model building. It is a branch of artificial intelligence based on the idea that systems can learn from data.",
        }
    
    def execute(self, task: str) -> Dict[str, Any]:
        """
        Generate documentation based on task
        
        Args:
            task: Documentation request
        
        Returns:
            Documentation content
        """
        if not self.validate_input(task):
            raise ValueError("Invalid documentation request")
        
        task_lower = task.lower()
        
        # Find matching topic
        matching_topic = None
        matching_content = None
        
        for topic, content in self.knowledge_base.items():
            if topic in task_lower:
                matching_topic = topic
                matching_content = content
                break
        
        if not matching_content:
            matching_content = f"Documentation for: {task}\n\nThis is a general explanation about the requested topic. For detailed documentation, please refer to official sources."
            matching_topic = "general"
        
        # Generate structured documentation
        documentation = f"""
# Documentation: {matching_topic.title()}

## Overview
{matching_content}

## Key Features
- Feature 1: Core functionality
- Feature 2: Advanced capabilities
- Feature 3: Integration support

## Usage Example
```python
# Example code snippet
# TODO: Add specific implementation
pass
```

## Best Practices
1. Follow coding standards
2. Write comprehensive tests
3. Document your code
4. Use version control

## Additional Resources
- Official documentation
- Community forums
- Tutorial guides
"""
        
        return {
            "task": task,
            "topic": matching_topic,
            "documentation": documentation.strip(),
            "format": "markdown"
        }
