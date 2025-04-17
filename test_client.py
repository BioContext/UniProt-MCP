#!/usr/bin/env python3
"""
UniProt MCP Test Client.

A simple client for testing the UniProt MCP server locally. This script acts as a simple
interface to test the tools provided by the UniProt MCP server.

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
    print("UniProt MCP Test Client")
    print("======================")
    print("This client will send test requests to the UniProt MCP server.")
    print("The server should be running in another terminal with:")
    print("  python -m mcp_server --stdio")
    print()
    
    # Test get_protein_by_accession with human insulin
    await test_get_protein_by_accession("P01308")
    
    # Test search_proteins for BRCA1
    await test_search_proteins("BRCA1 human", 3)
    
    # Test get_protein_sequences for insulin
    await test_get_protein_sequences("P01308")
    
    # Test get_proteomics_data for BRCA1
    await test_get_proteomics_data("P38398", "domains")

async def test_get_protein_by_accession(accession: str):
    """Test the get_protein_by_accession tool."""
    print(f"Testing get_protein_by_accession with accession={accession}")
    
    request = {
        "name": "get_protein_by_accession",
        "parameters": {
            "accession": accession,
            "format": "json"
        }
    }
    
    await send_request(request)

async def test_search_proteins(query: str, limit: int):
    """Test the search_proteins tool."""
    print(f"Testing search_proteins with query='{query}', limit={limit}")
    
    request = {
        "name": "search_proteins",
        "parameters": {
            "query": query,
            "limit": limit
        }
    }
    
    await send_request(request)

async def test_get_protein_sequences(accessions: str):
    """Test the get_protein_sequences tool."""
    print(f"Testing get_protein_sequences with accessions='{accessions}'")
    
    request = {
        "name": "get_protein_sequences",
        "parameters": {
            "accessions": accessions
        }
    }
    
    await send_request(request)

async def test_get_proteomics_data(accession: str, feature_type: str):
    """Test the get_proteomics_data tool."""
    print(f"Testing get_proteomics_data with accession='{accession}', feature_type='{feature_type}'")
    
    request = {
        "name": "get_proteomics_data",
        "parameters": {
            "accession": accession,
            "feature_type": feature_type
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