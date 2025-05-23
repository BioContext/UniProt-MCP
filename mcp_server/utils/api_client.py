"""
API Client Utility Module.

This module provides utility functions for making API requests to the UniProt services.
"""

import json
import logging
from typing import Any, Dict, List, Optional, Union

import httpx

# Constants for API configuration
USER_AGENT = "uniprot-mcp/1.0"
DEFAULT_TIMEOUT = 30.0  # in seconds

# Configure logging
logger = logging.getLogger(__name__)

async def make_api_request(
    url: str,
    method: str = "GET",
    params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_data: Optional[Dict[str, Any]] = None,
    timeout: float = DEFAULT_TIMEOUT,
    return_text: bool = False
) -> Optional[Union[Dict[str, Any], str]]:
    """
    Make an API request to the UniProt API.
    
    Args:
        url: The URL to make the request to.
        method: The HTTP method to use (GET, POST, etc.).
        params: Optional query parameters to include in the request.
        headers: Optional headers to include in the request.
        json_data: Optional JSON data to include in the request body.
        timeout: Request timeout in seconds.
        return_text: If True, return the response as text instead of JSON.
        
    Returns:
        The parsed JSON response as a dictionary, the text response as a string,
        or None if the request failed.
    """
    # Prepare headers
    request_headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
    }
    
    # Update headers with any custom ones
    if headers:
        request_headers.update(headers)
    
    # Create async HTTP client
    async with httpx.AsyncClient() as client:
        try:
            # Make the request
            response = await client.request(
                method=method,
                url=url,
                params=params,
                headers=request_headers,
                json=json_data,
                timeout=timeout
            )
            
            # Raise an exception for bad status codes
            response.raise_for_status()
            
            # Return the response as text or JSON based on the return_text parameter
            if return_text:
                return response.text
            else:
                return response.json()
            
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error: {e.response.status_code} - {e.response.text}")
            return None
            
        except httpx.RequestError as e:
            logger.error(f"Request error: {str(e)}")
            return None
            
        except json.JSONDecodeError:
            if return_text:
                # If we're expecting text, try to return the text content
                try:
                    return response.text
                except Exception as e:
                    logger.error(f"Failed to get text response: {str(e)}")
                    return None
            else:
                logger.error("Failed to parse JSON response")
                return None
            
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return None

# TODO: Add any additional API client utility functions here 