"""Sample Agent Task - Hello World

Demonstrates how to create a custom agent task.
"""

from codev_agent import CodevAgent


def greet_user(name: str, greeting: str = "Hello") -> str:
    """A simple greeting task.
    
    Args:
        name: Name of the person to greet
        greeting: Greeting word (default: 'Hello')
    
    Returns:
        A personalized greeting message
    """
    return f"{greeting}, {name}! This is a custom Codev agent task."


def add_numbers(a: int, b: int) -> int:
    """Add two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    return a + b


def main():
    """Register and test sample tasks."""
    # Initialize agent
    agent = CodevAgent(name="SampleTaskAgent")
    
    # Register custom tasks
    agent.register_tool(
        'greet_user',
        greet_user,
        'Greet a user with a custom message'
    )
    
    agent.register_tool(
        'add_numbers',
        add_numbers,
        'Add two numbers together'
    )
    
    print("\n=== Sample Agent Tasks Demo ===")
    print(f"Agent: {agent.name}")
    print(f"Available tasks: {len(agent.list_tools())}\n")
    
    # Test greet_user task
    result1 = agent.execute_task('greet_user', name='Alice', greeting='Hi')
    print(f"Task 1: {result1['task']}")
    print(f"Status: {result1['status']}")
    print(f"Result: {result1['result']}\n")
    
    # Test add_numbers task
    result2 = agent.execute_task('add_numbers', a=42, b=58)
    print(f"Task 2: {result2['task']}")
    print(f"Status: {result2['status']}")
    print(f"Result: {result2['result']}\n")
    
    # Test hello_world (default task from registry)
    result3 = agent.execute_task('hello_world', name='Codev User')
    print(f"Task 3: {result3['task']}")
    print(f"Status: {result3['status']}")
    print(f"Result: {result3['result']}\n")
    
    print("=== Task History ===")
    for i, task in enumerate(agent.get_task_history(), 1):
        print(f"{i}. {task['task']} - {task['status']}")


if __name__ == '__main__':
    main()
