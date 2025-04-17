"""
Tests for the API client utility functions.
"""

import pytest
import httpx
from unittest.mock import AsyncMock, patch

from mcp_server.utils.api_client import make_api_request

# Example test for the make_api_request function
@pytest.mark.asyncio
async def test_make_api_request_success():
    """Test that make_api_request successfully handles a good response."""
    # Mock the httpx.AsyncClient.request method
    mock_response = AsyncMock()
    mock_response.status_code = 200
    mock_response.raise_for_status = AsyncMock()
    mock_response.json = AsyncMock(return_value={"key": "value"})
    
    with patch("httpx.AsyncClient.request", return_value=mock_response):
        result = await make_api_request("https://example.com/api")
        
    assert result == {"key": "value"}

@pytest.mark.asyncio
async def test_make_api_request_http_error():
    """Test that make_api_request handles HTTP errors properly."""
    # Mock the httpx.AsyncClient.request method to raise an HTTPStatusError
    mock_response = AsyncMock()
    mock_response.status_code = 404
    mock_response.text = "Not Found"
    mock_response.raise_for_status = AsyncMock(side_effect=httpx.HTTPStatusError(
        "404 Not Found", request=AsyncMock(), response=mock_response
    ))
    
    with patch("httpx.AsyncClient.request", return_value=mock_response):
        result = await make_api_request("https://example.com/api")
        
    assert result is None

@pytest.mark.asyncio
async def test_make_api_request_request_error():
    """Test that make_api_request handles general request errors properly."""
    # Mock the httpx.AsyncClient.request method to raise a RequestError
    with patch("httpx.AsyncClient.request", side_effect=httpx.RequestError("Connection error", request=AsyncMock())):
        result = await make_api_request("https://example.com/api")
        
    assert result is None 