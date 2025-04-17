FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY pyproject.toml ./
COPY README.md ./
COPY LICENSE ./

# Install the package
RUN pip install --no-cache-dir .

# Copy the application code
COPY mcp_server/ ./mcp_server/

# Run the MCP server with stdio transport by default
ENTRYPOINT ["python", "-m", "mcp_server", "--stdio"]

# Alternatively, to run as an HTTP server:
# CMD ["python", "-m", "mcp_server", "--transport", "http", "--host", "0.0.0.0", "--port", "8000"] 