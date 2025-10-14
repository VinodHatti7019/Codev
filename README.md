# Codev - AI Agent Automation System
The Vinod-powered AI Agent Automation playground - Your signature AI agent builder

## 🚀 Overview

Codev is a Python-based AI Agent Automation system that allows you to execute tasks using various tools through both CLI and web interfaces. The system includes a tool registry for search, code generation, and documentation APIs, with real-time logging and task execution tracking.

## ✨ Features

- **Main Agent Class**: Intelligent task handling and orchestration
- **Tool Registry**: Extensible system with built-in tools:
  - 🔍 **Search Tool**: Search for information across various sources
  - 💻 **Code Generator**: Generate code snippets based on requirements
  - 📚 **Documentation Tool**: Create and retrieve documentation
- **Dual Interface**: 
  - Command-line interface (CLI) for terminal users
  - Web interface for browser-based interaction
- **Real-time Logging**: Track task execution with detailed logs
- **Task History**: View all executed tasks and their results

## 📋 Requirements

- Python 3.7 or higher
- pip (Python package manager)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/VinodHatti7019/Codev.git
   cd Codev
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Linux/Mac:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

### Web Interface

Launch the web interface to interact with the agent through your browser:

```bash
python main.py web
```

The web interface will be available at `http://localhost:5000`

#### Web Interface Options:
```bash
# Custom host and port
python main.py web --host 127.0.0.1 --port 8080

# Production mode (disable debug)
python main.py web --no-debug
```

**Web Interface Features:**
- Interactive task input form
- Real-time result display
- Task history viewer
- Available tools overview

### Command-Line Interface (CLI)

#### Interactive Mode

Start an interactive session:

```bash
python main.py cli interactive
```

In interactive mode, you can:
- Type tasks directly and press Enter to execute
- Use `tools` to list available tools
- Use `history` to view task history
- Use `exit` or `quit` to exit

#### Execute Single Task

Execute a task directly:

```bash
python main.py cli execute "Search for Python tutorials"
```

Execute with a specific tool:

```bash
python main.py cli execute "Generate a REST API function" --tool code_generator
```

#### List Available Tools

```bash
python main.py cli list-tools
```

#### View Tool Information

```bash
python main.py cli tool-info search
```

#### View Task History

```bash
python main.py cli history
```

## 📖 Examples

### Example 1: Search for Information
```bash
python main.py cli execute "Search for machine learning"
```

### Example 2: Generate Code
```bash
python main.py cli execute "Generate a Python function to calculate factorial"
```

### Example 3: Get Documentation
```bash
python main.py cli execute "Document Flask framework"
```

### Example 4: Using Specific Tool
```bash
python main.py cli execute "Create API endpoint" --tool code_generator
```

## 🏗️ Project Structure

```
Codev/
├── agent_system/           # Main package
│   ├── __init__.py
│   ├── agent.py           # Main agent class
│   ├── tool_registry.py   # Tool management
│   ├── cli.py            # CLI interface
│   ├── tools/            # Tools package
│   │   ├── __init__.py
│   │   ├── base_tool.py  # Base tool class
│   │   ├── search_tool.py
│   │   ├── code_generator.py
│   │   └── docs_tool.py
│   └── web/              # Web interface
│       ├── __init__.py
│       ├── app.py        # Flask application
│       ├── templates/
│       │   └── index.html
│       └── static/
│           ├── css/
│           │   └── style.css
│           └── js/
│               └── script.js
├── main.py               # Main entry point
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── LICENSE              # MIT License
```

## 🔧 Extending the System

### Adding a New Tool

1. Create a new tool class in `agent_system/tools/`:

```python
from .base_tool import BaseTool

class MyCustomTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="my_tool",
            description="Description of my tool"
        )
    
    def execute(self, task: str):
        # Implement your tool logic
        return {"result": "Custom result"}
```

2. Register the tool in `agent_system/tool_registry.py`:

```python
from .tools import MyCustomTool

class ToolRegistry:
    def _register_default_tools(self):
        # ... existing tools ...
        self.register_tool(MyCustomTool())
```

## 🌐 API Endpoints

When running the web interface, the following API endpoints are available:

- `POST /api/execute` - Execute a task
  ```json
  {
    "task": "Search for Python",
    "tool": "search"  // optional
  }
  ```

- `GET /api/tools` - List all available tools
- `GET /api/history` - Get task execution history
- `GET /api/task/<task_id>` - Get specific task details
- `GET /health` - Health check endpoint

## 🐛 Troubleshooting

### Port Already in Use

If port 5000 is already in use, specify a different port:
```bash
python main.py web --port 8080
```

### Import Errors

Make sure you've activated your virtual environment and installed all dependencies:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Vinod Hatti**

- GitHub: [@VinodHatti7019](https://github.com/VinodHatti7019)

## 🙏 Acknowledgments

- Built with Flask for the web interface
- Inspired by modern AI agent architectures
- Designed for extensibility and ease of use

---

**Happy Automating! 🤖**
