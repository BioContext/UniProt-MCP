# Contributing to Uniprot MCP

Thank you for considering contributing to the Uniprot MCP! This document outlines the process for contributing to this project.

## Code of Conduct

Please be respectful and considerate when contributing to this project. Harassment or inappropriate behavior will not be tolerated.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion for improvement:

1. Check if the issue already exists in the [issue tracker](https://github.com/yourusername/MCP-Server-Boilerplate/issues)
2. If not, create a new issue with:
   - A clear title
   - A detailed description of the issue
   - Steps to reproduce (if applicable)
   - Expected and actual behavior
   - Screenshots (if applicable)
   - Environment information (OS, Python version, etc.)

### Submitting Changes

To submit changes:

1. Fork the repository
2. Create a new branch for your change:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes
4. Run tests to ensure they pass:
   ```bash
   pytest
   ```
5. Format your code:
   ```bash
   black mcp_server tests
   isort mcp_server tests
   ```
6. Commit your changes with a descriptive commit message
7. Push your branch to your fork
8. Submit a pull request to the main repository

### Pull Request Process

1. Ensure your PR includes a description of the changes and the issue it addresses
2. Update the README.md or documentation with any necessary changes
3. Ensure all tests pass
4. A maintainer will review your PR and may request changes
5. Once approved, a maintainer will merge your PR

## Development Environment

To set up your development environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MCP-Server-Boilerplate.git
   cd MCP-Server-Boilerplate
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e '.[dev]'
   ```

## Coding Standards

Please follow these coding standards:

- Use [Black](https://black.readthedocs.io/) for code formatting
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines
- Write docstrings for all functions, classes, and modules
- Include type hints for all function arguments and return values

## License

By contributing to this project, you agree that your contributions will be licensed under the project's [MIT License](LICENSE). 