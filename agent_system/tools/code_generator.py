"""
Code Generator Tool
Generates code snippets based on task description
"""

from typing import Dict, Any
from .base_tool import BaseTool


class CodeGeneratorTool(BaseTool):
    """Tool for generating code snippets"""
    
    def __init__(self):
        super().__init__(
            name="code_generator",
            description="Generate code snippets based on requirements"
        )
        self.templates = {
            "python": {
                "function": '''def {name}({params}):
    """
    {description}
    """
    # TODO: Implement function logic
    pass
''',
                "class": '''class {name}:
    """
    {description}
    """
    
    def __init__(self):
        pass
''',
                "api": '''from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/{endpoint}', methods=['GET'])
def {endpoint}():
    """
    {description}
    """
    return jsonify({{"status": "success", "data": {{}}}})

if __name__ == '__main__':
    app.run(debug=True)
'''
            }
        }
    
    def execute(self, task: str) -> Dict[str, Any]:
        """
        Generate code based on task description
        
        Args:
            task: Code generation task
        
        Returns:
            Generated code snippet
        """
        if not self.validate_input(task):
            raise ValueError("Invalid code generation request")
        
        task_lower = task.lower()
        
        # Determine code type
        if "function" in task_lower:
            code_type = "function"
            template = self.templates["python"]["function"]
            code = template.format(
                name="example_function",
                params="param1, param2",
                description=task
            )
        elif "class" in task_lower:
            code_type = "class"
            template = self.templates["python"]["class"]
            code = template.format(
                name="ExampleClass",
                description=task
            )
        elif "api" in task_lower or "endpoint" in task_lower:
            code_type = "api"
            template = self.templates["python"]["api"]
            code = template.format(
                endpoint="example",
                description=task
            )
        else:
            # Default to function
            code_type = "function"
            template = self.templates["python"]["function"]
            code = template.format(
                name="generated_function",
                params="*args, **kwargs",
                description=task
            )
        
        return {
            "task": task,
            "language": "python",
            "code_type": code_type,
            "code": code,
            "status": "generated"
        }
