# Contributing to HackTheGrow-HeyAbby

First off, thank you for considering contributing to HackTheGrow-HeyAbby! 🎉

This document provides guidelines for contributing to the project. Following these guidelines helps maintain code quality and makes the review process smoother for everyone.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Testing](#testing)
- [Documentation](#documentation)

---

## 🤝 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of:

- Experience level
- Gender identity and expression
- Sexual orientation
- Disability
- Personal appearance
- Body size
- Race
- Ethnicity
- Age
- Religion
- Nationality

### Expected Behavior

- Be respectful and considerate in your communication
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other contributors

### Unacceptable Behavior

- Harassment, trolling, or insulting comments
- Personal or political attacks
- Public or private harassment
- Publishing others' private information without permission
- Any conduct that would be inappropriate in a professional setting

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic understanding of HTTP requests and web APIs
- Familiarity with security testing concepts

### First Time Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/HackTheGrow-HeyAbby.git
   cd HackTheGrow-HeyAbby
   ```
3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/AfterPacket/HackTheGrow-HeyAbby.git
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

---

## 💡 How to Contribute

### Types of Contributions

We welcome various types of contributions:

- 🐛 **Bug fixes** - Fix issues and improve stability
- ✨ **New features** - Add functionality that enhances the tool
- 📝 **Documentation** - Improve README, comments, or guides
- 🧪 **Tests** - Add or improve test coverage
- 🎨 **Code quality** - Refactoring, optimization, or cleanup
- 🔒 **Security** - Address vulnerabilities or improve security

### Before You Start

1. **Check existing issues** - Someone might already be working on it
2. **Open an issue first** - For major changes, discuss your idea before implementing
3. **Get feedback** - Make sure your contribution aligns with project goals

---

## 🛠️ Development Setup

### Creating a Development Branch

Always work in a feature branch:

```bash
git checkout -b feature/your-feature-name
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Test additions or updates

### Keeping Your Fork Updated

Regularly sync with upstream:

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

---

## 📐 Coding Standards

### Python Style Guide

Follow [PEP 8](https://pep8.org/) guidelines:

```python
# Good
def send_request(url, headers, data):
    """Send a POST request to the specified URL.
    
    Args:
        url (str): The target URL
        headers (dict): Request headers
        data (dict): Request payload
        
    Returns:
        requests.Response: The response object
    """
    response = requests.post(url, headers=headers, json=data)
    return response

# Bad
def sendRequest(url,headers,data):
    resp=requests.post(url,headers=headers,json=data)
    return resp
```

### Best Practices

- ✅ Use descriptive variable names
- ✅ Write docstrings for all functions
- ✅ Keep functions focused and small
- ✅ Handle exceptions appropriately
- ✅ Add comments for complex logic
- ❌ Don't hardcode credentials or sensitive data
- ❌ Avoid overly nested code
- ❌ Don't commit commented-out code

### Security Considerations

When contributing to a security tool:

- Never include real credentials or API keys
- Use placeholder values in examples
- Validate all user inputs
- Follow secure coding practices
- Be mindful of potential security implications

---

## 📝 Commit Guidelines

### Commit Message Format

Use clear, descriptive commit messages:

```
Type: Short summary (50 chars or less)

More detailed explanation if needed. Wrap at 72 characters.
Explain what and why, not how.

- Additional bullet points if needed
- Can include multiple items

Fixes #123
```

### Commit Types

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, no logic change)
- `refactor:` - Code refactoring
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

### Examples

```bash
# Good commits
git commit -m "feat: Add support for custom timeout values"
git commit -m "fix: Resolve issue with malformed headers"
git commit -m "docs: Update installation instructions"

# Bad commits
git commit -m "fixed stuff"
git commit -m "updates"
git commit -m "asdf"
```

---

## 🔄 Pull Request Process

### Before Submitting

- ✅ Test your changes thoroughly
- ✅ Update documentation if needed
- ✅ Ensure code follows style guidelines
- ✅ Write clear commit messages
- ✅ Rebase on latest main branch

### Submitting a Pull Request

1. **Push your branch** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open a pull request** on GitHub with:
   - Clear title describing the change
   - Detailed description of what and why
   - Reference any related issues
   - Screenshots/examples if applicable

3. **Pull request template**:
   ```markdown
   ## Description
   Brief description of the changes

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Code refactoring

   ## Testing
   Describe how you tested these changes

   ## Checklist
   - [ ] Code follows project style guidelines
   - [ ] Documentation updated
   - [ ] Tests added/updated
   - [ ] All tests pass
   
   ## Related Issues
   Fixes #123
   ```

### Review Process

- Maintainers will review your PR
- Address any requested changes
- Once approved, your PR will be merged
- Celebrate your contribution! 🎉

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_requests.py

# Run with coverage
python -m pytest --cov=.
```

### Writing Tests

Add tests for new features:

```python
import pytest
from your_module import send_request

def test_send_request_success():
    """Test successful POST request."""
    url = "https://httpbin.org/post"
    headers = {"Content-Type": "application/json"}
    data = {"test": "value"}
    
    response = send_request(url, headers, data)
    
    assert response.status_code == 200
    assert "test" in response.json()["json"]
```

---

## 📚 Documentation

### What to Document

- **Code comments** - Explain complex logic
- **Docstrings** - Document all functions and classes
- **README updates** - Keep user-facing docs current
- **Examples** - Add usage examples for new features

### Documentation Style

```python
def analyze_response(response, expected_code=200):
    """Analyze HTTP response and validate status code.
    
    This function checks if the response status code matches
    the expected value and extracts relevant information.
    
    Args:
        response (requests.Response): The HTTP response object
        expected_code (int, optional): Expected status code. 
            Defaults to 200.
    
    Returns:
        dict: Dictionary containing:
            - success (bool): Whether validation passed
            - status (int): Actual status code
            - message (str): Result message
    
    Raises:
        ValueError: If response is None
        
    Example:
        >>> resp = requests.get("https://example.com")
        >>> result = analyze_response(resp)
        >>> print(result['success'])
        True
    """
    # Implementation here
    pass
```

---

## ❓ Questions?

If you have questions or need help:

- 📖 Check existing documentation
- 🔍 Search existing issues
- 💬 Open a new issue for discussion
- 📧 Contact HeyAbby: support@heyabby.com

---

## 🙏 Thank You!

Your contributions make this project better for everyone. We appreciate your time and effort!

**Happy coding!** 🚀🔒
