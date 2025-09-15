# Contributing to DataUtils

Thank you for considering contributing to DataUtils! We welcome contributions from the community to help improve this project.

## How to Contribute

1. **Fork** the repository on GitHub
2. **Clone** the project to your own machine
3. **Create a branch** for your feature or bug fix
4. **Commit** your changes to your branch
5. **Push** your work back up to your fork
6. Submit a **Pull Request**

## Development Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Install development dependencies:
   ```bash
   pip install -e .[dev]
   pre-commit install
   ```

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use type hints for all function signatures
- Include docstrings for all public methods and classes
- Keep lines under 88 characters (Black's default)

## Testing

Run the test suite with:
```bash
pytest
```

## Pull Request Process

1. Ensure any dependencies are properly documented
2. Update the README.md with details of changes if needed
3. Make sure all tests pass
4. Update the CHANGELOG.md with details of changes

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.
