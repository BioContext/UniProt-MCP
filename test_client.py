#!/usr/bin/env python3
"""
MCP Test Client.

A simple client for testing the MCP server locally. This script acts as a simple
interface to test the tools provided by the MCP server.

Usage:
    python test_client.py
"""

import asyncio
import json
import os
import sys
from typing import Any, Dict, List

async def main():
    """Run the test client."""
    print("MCP Test Client")
    print("==============")
    print("This client will send test requests to the MCP server.")
    print("The server should be running in another terminal with:")
    print("  python -m mcp_server --stdio")
    print()
    
    # Example test: get_data_by_id
    await test_get_data_by_id("example123")
    
    # Example test: search_items
    await test_search_items("example", 5)

async def test_get_data_by_id(item_id: str):
    """Test the get_data_by_id tool."""
    print(f"Testing get_data_by_id with item_id={item_id}")
    
    request = {
        "name": "get_data_by_id",
        "parameters": {
            "item_id": item_id
        }
    }
    
    await send_request(request)

async def test_search_items(query: str, max_results: int):
    """Test the search_items tool."""
    print(f"Testing search_items with query='{query}', max_results={max_results}")
    
    request = {
        "name": "search_items",
        "parameters": {
            "query": query,
            "max_results": max_results
        }
    }
    
    await send_request(request)

async def send_request(request: Dict[str, Any]):
    """Send a request to the MCP server and print the response."""
    request_json = json.dumps(request)
    print(f"Request: {request_json}")
    
    # In a real client, you would send the request to the server
    # and receive a response. Here we're just simulating it.
    print("Response would be received here in a real implementation.")
    print()

if __name__ == "__main__":
    asyncio.run(main()) 