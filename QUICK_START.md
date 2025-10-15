# Quick Start Guide

## Installation (30 seconds)

```bash
git clone https://github.com/VinodHatti7019/Codev.git
cd Codev
pip install -r requirements.txt
```

## Usage

### 🌐 Web Interface (Recommended for Beginners)

```bash
python main.py web
```

Then open http://localhost:5000 in your browser.

### 💻 CLI Interface

#### Interactive Mode (Best for Exploration)
```bash
python main.py cli interactive
```

#### Execute Single Tasks
```bash
# Search for information
python main.py cli execute "Search for Python tutorials"

# Generate code
python main.py cli execute "Generate a Python class" --tool code_generator

# Get documentation
python main.py cli execute "Document Flask framework" --tool docs
```

#### Other Commands
```bash
# List all available tools
python main.py cli list-tools

# Get tool information
python main.py cli tool-info search

# View task history
python main.py cli history
```

### 🐍 Programmatic Usage

```python
from agent_system.agent import Agent

# Create an agent
agent = Agent("MyAgent")

# Execute tasks
result = agent.execute_task("Search for machine learning")

# Access results
print(result['status'])      # 'completed'
print(result['result'])      # Task output
print(result['tool_used'])   # Tool that was used

# View history
history = agent.get_task_history()
```

## Available Tools

| Tool | Description | Example Usage |
|------|-------------|---------------|
| **search** | Search for information | "Search for Python" |
| **code_generator** | Generate code snippets | "Generate a REST API function" |
| **docs** | Create documentation | "Document Flask framework" |

## Web API Endpoints

When running the web interface, the following REST API endpoints are available:

- `POST /api/execute` - Execute a task
- `GET /api/tools` - List all tools
- `GET /api/history` - Get task history
- `GET /api/task/<id>` - Get specific task
- `GET /health` - Health check

### API Example

```bash
curl -X POST http://localhost:5000/api/execute \
  -H "Content-Type: application/json" \
  -d '{"task": "Search for Python", "tool": "search"}'
```

## Tips

1. **Interactive Mode**: Best for exploring and testing
2. **Web Interface**: Best for visual feedback and ease of use
3. **CLI Execute**: Best for automation and scripting
4. **Programmatic**: Best for integration with other Python code

## Need Help?

- Check the main [README.md](README.md) for detailed documentation
- Run `python main.py cli --help` for CLI options
- Run `python main.py cli interactive` and type `tools` to see available tools
