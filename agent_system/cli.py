"""
CLI Interface
Command-line interface for the AI Agent
"""

import sys
import argparse
from typing import Optional
from .agent import Agent


class CLI:
    """Command-line interface for agent interaction"""
    
    def __init__(self):
        """Initialize CLI"""
        self.agent = Agent()
        self.parser = self._setup_parser()
    
    def _setup_parser(self) -> argparse.ArgumentParser:
        """Setup command-line argument parser"""
        parser = argparse.ArgumentParser(
            description="AI Agent Automation System",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  %(prog)s execute "Search for Python tutorials"
  %(prog)s execute "Generate a REST API function" --tool code_generator
  %(prog)s list-tools
  %(prog)s history
  %(prog)s interactive
            """
        )
        
        subparsers = parser.add_subparsers(dest="command", help="Available commands")
        
        # Execute command
        execute_parser = subparsers.add_parser("execute", help="Execute a task")
        execute_parser.add_argument("task", help="Task description")
        execute_parser.add_argument("--tool", "-t", help="Specific tool to use")
        
        # List tools command
        subparsers.add_parser("list-tools", help="List all available tools")
        
        # Tool info command
        info_parser = subparsers.add_parser("tool-info", help="Get information about a tool")
        info_parser.add_argument("tool_name", help="Name of the tool")
        
        # History command
        subparsers.add_parser("history", help="Show task execution history")
        
        # Interactive mode command
        subparsers.add_parser("interactive", help="Start interactive mode")
        
        return parser
    
    def execute_task(self, task: str, tool: Optional[str] = None):
        """Execute a single task"""
        print(f"\n{'='*60}")
        print(f"Executing task: {task}")
        print(f"{'='*60}\n")
        
        result = self.agent.execute_task(task, tool)
        
        self._print_result(result)
    
    def _print_result(self, result: dict):
        """Print task execution result"""
        print(f"\nTask ID: {result['task_id']}")
        print(f"Status: {result['status']}")
        print(f"Tool Used: {result['tool_used']}")
        print(f"Duration: {result['duration']:.2f} seconds")
        
        if result['status'] == 'completed':
            print("\n--- Result ---")
            if isinstance(result['result'], dict):
                for key, value in result['result'].items():
                    if key == 'code' or key == 'documentation':
                        print(f"\n{key.upper()}:")
                        print(value)
                    elif key == 'results' and isinstance(value, list):
                        print(f"\n{key.upper()}:")
                        for i, item in enumerate(value, 1):
                            print(f"  {i}. {item}")
                    else:
                        print(f"{key}: {value}")
            else:
                print(result['result'])
        else:
            print(f"\nError: {result['error']}")
        
        print(f"\n{'='*60}\n")
    
    def list_tools(self):
        """List all available tools"""
        tools = self.agent.list_tools()
        print("\n=== Available Tools ===\n")
        for tool_name in tools:
            info = self.agent.get_tool_info(tool_name)
            print(f"- {info['name']}: {info['description']}")
        print()
    
    def show_tool_info(self, tool_name: str):
        """Show detailed information about a tool"""
        try:
            info = self.agent.get_tool_info(tool_name)
            print(f"\n=== Tool: {info['name']} ===\n")
            print(f"Description: {info['description']}")
            print(f"Version: {info['version']}")
            print()
        except KeyError:
            print(f"\nError: Tool '{tool_name}' not found\n")
    
    def show_history(self):
        """Show task execution history"""
        history = self.agent.get_task_history()
        
        if not history:
            print("\nNo tasks executed yet.\n")
            return
        
        print("\n=== Task History ===\n")
        for task in history:
            print(f"Task #{task['task_id']}: {task['task']}")
            print(f"  Status: {task['status']}")
            print(f"  Tool: {task['tool_used']}")
            print(f"  Duration: {task['duration']:.2f}s")
            print()
    
    def interactive_mode(self):
        """Start interactive mode"""
        print("\n" + "="*60)
        print("AI Agent Interactive Mode")
        print("="*60)
        print("\nCommands:")
        print("  - Type your task to execute it")
        print("  - 'tools' - List available tools")
        print("  - 'history' - Show task history")
        print("  - 'exit' or 'quit' - Exit interactive mode")
        print("\n" + "="*60 + "\n")
        
        while True:
            try:
                user_input = input("\nAgent> ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ["exit", "quit"]:
                    print("\nGoodbye!\n")
                    break
                
                if user_input.lower() == "tools":
                    self.list_tools()
                    continue
                
                if user_input.lower() == "history":
                    self.show_history()
                    continue
                
                # Execute as task
                result = self.agent.execute_task(user_input)
                self._print_result(result)
                
            except KeyboardInterrupt:
                print("\n\nGoodbye!\n")
                break
            except Exception as e:
                print(f"\nError: {str(e)}\n")
    
    def run(self, args=None):
        """Run the CLI"""
        parsed_args = self.parser.parse_args(args)
        
        if not parsed_args.command:
            self.parser.print_help()
            return
        
        if parsed_args.command == "execute":
            self.execute_task(parsed_args.task, parsed_args.tool)
        elif parsed_args.command == "list-tools":
            self.list_tools()
        elif parsed_args.command == "tool-info":
            self.show_tool_info(parsed_args.tool_name)
        elif parsed_args.command == "history":
            self.show_history()
        elif parsed_args.command == "interactive":
            self.interactive_mode()


def main():
    """Main entry point for CLI"""
    cli = CLI()
    cli.run()


if __name__ == "__main__":
    main()
