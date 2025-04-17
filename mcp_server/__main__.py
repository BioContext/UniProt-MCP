"""
Main entry point for the MCP server.

This module provides the command-line interface for running the MCP server.
"""

import argparse
import sys
from mcp_server import run

def main():
    """
    Main entry point for running the MCP server from the command line.
    Parses arguments and starts the server in the appropriate mode.
    """
    parser = argparse.ArgumentParser(description='MCP Server')
    parser.add_argument('--port', type=int, default=8000, 
                        help='Port to run the server on (when not using stdio)')
    parser.add_argument('--host', type=str, default='127.0.0.1', 
                        help='Host to bind the server to (when not using stdio)')
    parser.add_argument('--stdio', action='store_true', 
                        help='Run in stdio mode for MCP (default when used with Claude Desktop)')
    parser.add_argument('--transport', type=str, choices=['stdio', 'http', 'websocket'],
                        default='stdio', help='Transport method to use')
    
    args = parser.parse_args()
    
    # Determine the transport method
    transport = 'stdio' if args.stdio else args.transport
    
    if transport == 'stdio':
        # Run in stdio mode for MCP (used by Claude Desktop and other clients)
        run(transport='stdio')
    elif transport == 'http':
        # Run as a web server
        import uvicorn
        from mcp_server import mcp
        uvicorn.run(
            app=mcp.app,
            host=args.host,
            port=args.port,
            log_level="info"
        )
    else:
        print(f"Transport method '{transport}' not implemented yet", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 