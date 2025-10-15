#!/usr/bin/env python3
"""
Example Usage Script
Demonstrates how to use the Codev AI Agent programmatically
"""

from agent_system.agent import Agent


def main():
    """Run examples"""
    print("=" * 60)
    print("Codev AI Agent - Example Usage")
    print("=" * 60)
    print()
    
    # Create an agent
    agent = Agent("ExampleAgent")
    
    # Example 1: Search for information
    print("Example 1: Search Task")
    print("-" * 60)
    result = agent.execute_task("Search for Python programming")
    print(f"Status: {result['status']}")
    print(f"Tool Used: {result['tool_used']}")
    print(f"Results: {result['result']['num_results']} found")
    print()
    
    # Example 2: Generate code
    print("Example 2: Code Generation")
    print("-" * 60)
    result = agent.execute_task("Generate a function to calculate fibonacci")
    print(f"Status: {result['status']}")
    print(f"Tool Used: {result['tool_used']}")
    print("Generated Code:")
    print(result['result']['code'])
    print()
    
    # Example 3: Get documentation
    print("Example 3: Documentation Request")
    print("-" * 60)
    result = agent.execute_task("Document Python language")
    print(f"Status: {result['status']}")
    print(f"Tool Used: {result['tool_used']}")
    print("Documentation:")
    print(result['result']['documentation'][:200] + "...")
    print()
    
    # Example 4: List all tools
    print("Example 4: Available Tools")
    print("-" * 60)
    tools = agent.list_tools()
    for tool_name in tools:
        info = agent.get_tool_info(tool_name)
        print(f"- {info['name']}: {info['description']}")
    print()
    
    # Example 5: View task history
    print("Example 5: Task History")
    print("-" * 60)
    history = agent.get_task_history()
    print(f"Total tasks executed: {len(history)}")
    for task in history:
        print(f"  Task #{task['task_id']}: {task['task'][:50]}... - {task['status']}")
    print()
    
    print("=" * 60)
    print("Examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
