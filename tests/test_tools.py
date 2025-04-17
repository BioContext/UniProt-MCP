"""
Tests for the API tool functions.
"""

import pytest
from unittest.mock import AsyncMock, patch

from mcp_server.api.tools import get_data_by_id, search_items

# Example test for the get_data_by_id tool function
@pytest.mark.asyncio
async def test_get_data_by_id_success():
    """Test that get_data_by_id successfully returns data when the API request succeeds."""
    mock_data = {
        "id": "123",
        "name": "Test Item",
        "description": "This is a test item."
    }
    
    # Mock the make_api_request function
    with patch("mcp_server.api.tools.make_api_request", return_value=mock_data):
        result = await get_data_by_id("123")
        
    assert result == mock_data

@pytest.mark.asyncio
async def test_get_data_by_id_failure():
    """Test that get_data_by_id returns an error message when the API request fails."""
    # Mock the make_api_request function to return None (indicating failure)
    with patch("mcp_server.api.tools.make_api_request", return_value=None):
        result = await get_data_by_id("123")
        
    assert "error" in result
    assert result["error"] == "Unable to fetch data or item not found."

# Example test for the search_items tool function
@pytest.mark.asyncio
async def test_search_items_success():
    """Test that search_items successfully returns formatted results when the API request succeeds."""
    mock_data = {
        "results": [
            {
                "id": "123",
                "name": "Test Item 1",
                "description": "Description 1"
            },
            {
                "id": "456",
                "name": "Test Item 2",
                "description": "Description 2"
            }
        ]
    }
    
    expected_results = [
        {
            "id": "123",
            "name": "Test Item 1",
            "description": "Description 1"
        },
        {
            "id": "456",
            "name": "Test Item 2",
            "description": "Description 2"
        }
    ]
    
    # Mock the make_api_request function
    with patch("mcp_server.api.tools.make_api_request", return_value=mock_data):
        result = await search_items("test", 10)
        
    assert result == expected_results

@pytest.mark.asyncio
async def test_search_items_no_results():
    """Test that search_items returns an empty list when there are no results."""
    mock_data = {"results": []}
    
    # Mock the make_api_request function
    with patch("mcp_server.api.tools.make_api_request", return_value=mock_data):
        result = await search_items("test", 10)
        
    assert result == []

@pytest.mark.asyncio
async def test_search_items_failure():
    """Test that search_items returns an empty list when the API request fails."""
    # Mock the make_api_request function to return None (indicating failure)
    with patch("mcp_server.api.tools.make_api_request", return_value=None):
        result = await search_items("test", 10)
        
    assert result == [] 