"""
MCP Server Initialization module.

This module initializes the MCP server with the FastMCP implementation.
"""

from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server with your service name
# TODO: Change 'uniprot' to the actual name of your API service
mcp = FastMCP("uniprot")

# Import all tool modules to register them with the MCP server
# This imports all the tool functions from the API module
from .api import tools

# Export the MCP instance for use in other modules
__all__ = ["mcp"]

# Function to run the MCP server
def run(transport='stdio'):
    """
    Run the MCP server with the specified transport.
    
    Args:
        transport (str): The transport to use. Default is 'stdio'.
                         Other options include 'http' or 'websocket'.
    """
    mcp.run(transport=transport) 