#!/usr/bin/env python3
"""Codev CLI - Command Line Interface

Minimal CLI to invoke agent tasks.
"""

import sys
import argparse
import logging
from codev_agent import CodevAgent

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Codev Agent CLI - Execute agent tasks from command line'
    )
    
    parser.add_argument(
        'task',
        help='Task name to execute'
    )
    
    parser.add_argument(
        '-p', '--params',
        nargs='*',
        help='Task parameters in key=value format',
        default=[]
    )
    
    parser.add_argument(
        '-l', '--list',
        action='store_true',
        help='List all available tasks'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Initialize agent
    agent = CodevAgent()
    
    # List tasks
    if args.list:
        print("\nAvailable Tasks:")
        print("-" * 50)
        for tool in agent.list_tools():
            print(f"  {tool['name']:<20} {tool['description']}")
        print()
        return 0
    
    # Parse parameters
    params = {}
    for param in args.params:
        if '=' in param:
            key, value = param.split('=', 1)
            params[key] = value
        else:
            logger.warning(f"Ignoring invalid parameter: {param}")
    
    # Execute task
    try:
        print(f"\nExecuting task: {args.task}")
        result = agent.execute_task(args.task, **params)
        
        if result['status'] == 'success':
            print(f"✓ Success: {result['result']}")
            return 0
        else:
            print(f"✗ Failed: {result.get('error', 'Unknown error')}")
            return 1
    
    except Exception as e:
        logger.error(f"Execution failed: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
