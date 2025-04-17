"""
UniProt API Tool Functions Module.

This module contains tool functions that access the UniProt protein database API.
Each function is decorated with the @mcp.tool() decorator to register it with the MCP server.
"""

import httpx
from typing import Any, Dict, List, Optional, Union
from ..utils.api_client import make_api_request
from .. import mcp

# Constants for API configuration
API_BASE_URL = "https://rest.uniprot.org"
USER_AGENT = "uniprot-mcp/1.0"

@mcp.tool()
async def get_protein_by_accession(accession: str, format: str = "json") -> Dict[str, Any]:
    """
    Get detailed information about a protein by its UniProt accession number.
    
    Args:
        accession: The UniProt accession number (e.g., P12345).
        format: The format of the response (default: json).
        
    Returns:
        A dictionary containing the protein details.
    """
    # UniProt API endpoint for accessing a protein entry
    url = f"{API_BASE_URL}/uniprotkb/{accession}"
    
    # Setup headers for the requested format
    headers = {"Accept": f"application/{format}"}
    
    # Make the API request using our utility function
    response_data = await make_api_request(url, headers=headers)
    
    if not response_data:
        return {"error": f"Unable to fetch data for protein with accession {accession}."}
    
    return response_data

@mcp.tool()
async def search_proteins(query: str, fields: str = "accession,id,protein_name,gene_names,organism_name", limit: int = 10) -> List[Dict[str, Any]]:
    """
    Search for proteins matching the given query.
    
    Args:
        query: The search term or query (e.g., "insulin human").
        fields: Comma-separated list of fields to return (default: basic fields).
        limit: Maximum number of results to return (default: 10, max: 500).
        
    Returns:
        A list of matching proteins with their basic information.
    """
    # UniProt API endpoint for searching proteins
    url = f"{API_BASE_URL}/uniprotkb/search"
    
    # Setup parameters for the search request
    params = {
        "query": query,
        "fields": fields,
        "size": limit,
        "format": "json"
    }
    
    # Make the API request using our utility function
    response_data = await make_api_request(url, params=params)
    
    if not response_data or "results" not in response_data:
        return []
    
    return response_data.get("results", [])

@mcp.tool()
async def get_protein_sequences(accessions: str) -> Dict[str, Any]:
    """
    Get FASTA sequences for one or more proteins by their accession numbers.
    
    Args:
        accessions: Comma-separated list of UniProt accession numbers.
        
    Returns:
        A dictionary containing the sequences for the requested proteins.
    """
    # UniProt API endpoint for accessing sequences
    url = f"{API_BASE_URL}/uniprotkb/{accessions}.fasta"
    
    # Make the API request using our utility function with text response
    headers = {"Accept": "text/plain"}
    response_text = await make_api_request(url, headers=headers, return_text=True)
    
    if not response_text:
        return {"error": f"Unable to fetch sequences for accessions {accessions}."}
    
    # Parse the FASTA response into a structured format
    sequences = {}
    current_acc = None
    current_seq = []
    
    for line in response_text.splitlines():
        if line.startswith('>'):
            # New sequence header
            if current_acc:
                sequences[current_acc] = ''.join(current_seq)
            
            # Parse the accession from the header line
            header_parts = line[1:].split('|')
            if len(header_parts) > 1:
                current_acc = header_parts[1]
            else:
                current_acc = header_parts[0].split()[0]
            
            current_seq = []
        else:
            # Sequence line
            current_seq.append(line.strip())
    
    # Add the last sequence
    if current_acc:
        sequences[current_acc] = ''.join(current_seq)
    
    return {"sequences": sequences}

@mcp.tool()
async def get_proteomics_data(accession: str, feature_type: str = "all") -> Dict[str, Any]:
    """
    Get proteomics data for a protein, such as domains, variants, or PTMs.
    
    Args:
        accession: The UniProt accession number.
        feature_type: Type of feature to retrieve (e.g., "domains", "variants", "ptm", or "all").
        
    Returns:
        A dictionary containing the proteomics data.
    """
    # UniProt API endpoint for accessing feature annotations
    url = f"{API_BASE_URL}/uniprotkb/{accession}/features"
    
    # Setup parameters
    params = {}
    if feature_type != "all":
        params["categories"] = feature_type
    
    # Make the API request using our utility function
    response_data = await make_api_request(url, params=params)
    
    if not response_data:
        return {"error": f"Unable to fetch proteomics data for protein with accession {accession}."}
    
    return response_data 