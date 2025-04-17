# Uniprot MCP

A boilerplate for creating [Model Context Protocol (MCP)](https://modelcontextprotocol.io) servers that wrap existing APIs. This template makes it easy to quickly spin up new MCP servers that can be used with Claude for Desktop or other MCP clients.

## Overview

This boilerplate provides a standardized structure for creating MCP servers that expose third-party APIs as tools for LLMs. It includes:

- A modular architecture for easy customization
- Comprehensive documentation and examples
- Testing infrastructure
- Deployment configuration for Smithery

## Getting Started

### Prerequisites

- Python 3.10 or higher
- A third-party API you want to wrap

### Installation

1. Clone this repository and rename it for your API:

```bash
git clone https://github.com/yourusername/MCP-Server-Boilerplate.git my-api-mcp
cd my-api-mcp
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the dependencies:

```bash
pip install -e '.[dev]'
```

### Customization

To adapt this boilerplate for your API:

1. Update the service name in `mcp_server/__init__.py`
2. Modify `mcp_server/api/tools.py` to implement your API-specific tools
3. Update constants and configuration in `mcp_server/api/tools.py` and `mcp_server/utils/api_client.py`
4. Update the package metadata in `pyproject.toml`
5. Update the Smithery configuration in `smithery.yaml` if needed

### Running Your Server

To run your MCP server in development mode:

```bash
# Run with stdio transport (for Claude Desktop)
python -m mcp_server --stdio

# Or run as an HTTP server
python -m mcp_server --transport http --host 127.0.0.1 --port 8000
```

## Integrating with Claude for Desktop

1. Make sure you have [Claude for Desktop](https://www.anthropic.com/claude-downloads) installed and updated to the latest version.

2. Configure Claude for Desktop to use your MCP server by editing the configuration file:

```bash
# macOS
code ~/Library/Application\ Support/Claude/claude_desktop_config.json

# Windows
code %APPDATA%\Claude\claude_desktop_config.json
```

3. Add your server to the configuration:

```json
{
    "mcpServers": {
        "uniprot": {
            "command": "python",
            "args": [
                "-m",
                "mcp_server",
                "--stdio"
            ]
        }
    }
}
```

4. Restart Claude for Desktop and look for the hammer icon to verify your server is available.

## Directory Structure

```
├── mcp_server/              # Main package
│   ├── __init__.py          # MCP server initialization
│   ├── __main__.py          # Command-line entry point
│   ├── api/                 # API-specific code
│   │   ├── __init__.py
│   │   └── tools.py         # Tool functions that wrap API endpoints
│   └── utils/               # Utility functions
│       ├── __init__.py
│       └── api_client.py    # Helper for making API requests
├── tests/                   # Test suite
│   ├── __init__.py
│   ├── test_api_client.py
│   └── test_tools.py
├── Dockerfile               # Container configuration
├── LICENSE                  # License file
├── pyproject.toml           # Package metadata and dependencies
├── README.md                # This readme file
├── smithery.yaml            # Smithery deployment configuration
└── test_client.py           # Simple test client for local testing
```

## Testing

Run the test suite to verify your implementation:

```bash
pytest
```

You can also use the included test client to manually test your server:

```bash
python test_client.py
```

## Deployment

This boilerplate includes Smithery configuration for easy deployment. See the [Smithery documentation](https://smithery.ai/docs/deployment/llms.txt) for more details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 