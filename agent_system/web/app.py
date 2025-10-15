"""
Web Application
Flask web interface for the AI Agent
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from agent_system.agent import Agent


app = Flask(__name__)
agent = Agent("WebAgent")


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/api/execute', methods=['POST'])
def execute_task():
    """Execute a task via API"""
    data = request.get_json()
    
    if not data or 'task' not in data:
        return jsonify({"error": "Task is required"}), 400
    
    task = data['task']
    tool = data.get('tool')
    
    try:
        result = agent.execute_task(task, tool)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/tools', methods=['GET'])
def list_tools():
    """List all available tools"""
    tools = agent.list_tools()
    tool_info = []
    
    for tool_name in tools:
        info = agent.get_tool_info(tool_name)
        tool_info.append(info)
    
    return jsonify({"tools": tool_info})


@app.route('/api/history', methods=['GET'])
def get_history():
    """Get task execution history"""
    history = agent.get_task_history()
    return jsonify({"history": history})


@app.route('/api/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get specific task by ID"""
    task = agent.get_task_by_id(task_id)
    
    if task:
        return jsonify(task)
    else:
        return jsonify({"error": "Task not found"}), 404


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "agent": agent.name
    })


def run_server(host='0.0.0.0', port=5000, debug=True):
    """Run the Flask server"""
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    run_server()
