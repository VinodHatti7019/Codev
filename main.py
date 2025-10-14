#!/usr/bin/env python3
"""
Main Entry Point
Launch the AI Agent system via CLI or Web interface
"""

import sys
import argparse


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python main.py {cli|web} [options]")
        print("\nFor CLI mode: python main.py cli [cli-options]")
        print("For Web mode: python main.py web [--host HOST] [--port PORT] [--no-debug]")
        sys.exit(1)
    
    mode = sys.argv[1]
    
    if mode == 'cli':
        from agent_system.cli import CLI
        # Create CLI and pass remaining arguments
        cli = CLI()
        cli.run(sys.argv[2:])
    elif mode == 'web':
        # Parse web-specific arguments
        parser = argparse.ArgumentParser(
            description="Codev AI Agent Web Interface"
        )
        parser.add_argument(
            '--host',
            default='0.0.0.0',
            help='Host for web server (default: 0.0.0.0)'
        )
        parser.add_argument(
            '--port',
            type=int,
            default=5000,
            help='Port for web server (default: 5000)'
        )
        parser.add_argument(
            '--no-debug',
            action='store_true',
            help='Disable debug mode for web server'
        )
        args = parser.parse_args(sys.argv[2:])
        
        from agent_system.web.app import run_server
        print(f"\n🚀 Starting Codev AI Agent Web Interface...")
        print(f"📍 Server running at http://{args.host}:{args.port}")
        print(f"Press CTRL+C to quit\n")
        run_server(host=args.host, port=args.port, debug=not args.no_debug)
    else:
        print(f"Error: Invalid mode '{mode}'. Use 'cli' or 'web'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
