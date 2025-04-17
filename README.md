# UniProt MCP

A Model Context Protocol (MCP) server for accessing the UniProt protein database API. This server enables LLMs like Claude to retrieve information about proteins and proteomics data directly from UniProt.

## Overview

The UniProt MCP server provides a bridge between LLMs and the UniProt REST API, allowing Claude and other LLMs to:

- Retrieve detailed protein information by accession number
- Search for proteins by keywords, genes, or organisms
- Get protein sequences in FASTA format
- Access proteomics data such as domains, variants, and post-translational modifications

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Claude for Desktop (for easy integration) or another MCP client

### Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/UniProt-MCP.git
cd UniProt-MCP
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

### Running the Server

To run the UniProt MCP server in development mode:

```bash
# Run with stdio transport (for Claude Desktop)
python -m mcp_server --stdio

# Or run as an HTTP server
python -m mcp_server --transport http --host 127.0.0.1 --port 8000
```

## Integrating with Claude for Desktop

1. Make sure you have [Claude for Desktop](https://www.anthropic.com/claude-downloads) installed and updated to the latest version.

2. Configure Claude for Desktop to use the UniProt MCP server by editing the configuration file:

```bash
# macOS
code ~/Library/Application\ Support/Claude/claude_desktop_config.json

# Windows
code %APPDATA%\Claude\claude_desktop_config.json
```

3. Add the UniProt server to the configuration:

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

## Available Tools

### get_protein_by_accession

Retrieves detailed information about a protein by its UniProt accession number.

**Example in Claude:**
```
Can you please get information about the insulin protein with accession P01308?
```

### search_proteins

Searches for proteins matching a given query.

**Example in Claude:**
```
Search UniProt for proteins related to "BRCA1 cancer" and show me the top 5 results.
```

### get_protein_sequences

Retrieves the amino acid sequences for one or more proteins in FASTA format.

**Example in Claude:**
```
Get the protein sequence for P01308 (human insulin).
```

### get_proteomics_data

Retrieves proteomics data such as domains, variants, or post-translational modifications.

**Example in Claude:**
```
What are the domain features of the BRCA1 protein (P38398)?
```

## API Documentation

The UniProt MCP server uses the [UniProt REST API](https://www.uniprot.org/help/api_queries) to fetch data. For more details on the underlying API, refer to the official UniProt API documentation.

## Testing

Run the test suite to verify the implementation:

```bash
pytest
```

You can also use the included test client to manually test the server:

```bash
python test_client.py
```

## Deployment

This server includes Smithery configuration for easy deployment. See the [Smithery documentation](https://smithery.ai/docs/deployment/llms.txt) for deployment details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 