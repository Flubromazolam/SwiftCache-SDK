# Contributing to SwiftCache

First off, thank you for considering contributing to SwiftCache! 🎉

## Code of Conduct

Be respectful, inclusive, and professional in all interactions.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When you create a bug report, include:

- **Clear title and description**
- **Steps to reproduce**
- **Expected vs actual behavior**
- **Code samples** (if applicable)
- **Environment** (iOS version, Xcode version, Swift version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description**
- **Use case** and motivation
- **Example code** showing how it would work
- **Comparison** with alternatives (if applicable)

### Pull Requests

**Important:** All contributions must go through pull requests. Direct pushes to `main` are not allowed.

1. **Fork the repository** (don't clone directly)
2. **Create your branch** from `main`: `git checkout -b feature/amazing-feature`
3. **Follow the existing code style**
4. **Add tests** for new functionality
5. **Ensure all tests pass**: `swift test`
6. **Update documentation** as needed
7. **Commit your changes** with clear messages
8. **Push to your fork**: `git push origin feature/amazing-feature`
9. **Open a Pull Request** from your fork to the main repository
10. **Wait for review** - PRs will be reviewed and merged by maintainers

#### Pull Request Checklist

- [ ] Code follows Swift style guidelines
- [ ] Tests added and passing
- [ ] Documentation updated
- [ ] CHANGELOG.md updated (if applicable)
- [ ] No breaking changes (or clearly documented)
- [ ] Branch is up to date with main

## Development Setup

```bash
# Fork the repo on GitHub first, then:

# Clone YOUR fork
git clone https://github.com/YOUR_USERNAME/SwiftCache-SDK.git
cd SwiftCache-SDK

# Add upstream remote
git remote add upstream https://github.com/SudhirGadhvi/SwiftCache-SDK.git

# Open in Xcode
open Package.swift

# Create a feature branch
git checkout -b feature/your-feature-name

# Run tests
swift test
# OR
xcodebuild test -scheme SwiftCache
```

## Code Style

- Follow Swift API Design Guidelines
- Use meaningful variable/function names
- Add doc comments for public APIs
- Keep functions focused and small
- Write tests for new features

## Testing

- Write unit tests for new functionality
- Ensure existing tests still pass
- Aim for >80% code coverage
- Test on both iOS and macOS

## Documentation

- Update README.md if needed
- Add doc comments to public APIs
- Update getting-started.md for new features
- Add examples for complex features

## Git Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests

Examples:
```
Add progressive loading support (#123)
Fix memory leak in disk cache cleanup
Update documentation for async APIs
```

## Release Process

1. Update version in Package.swift
2. Update CHANGELOG.md
3. Create git tag
4. Push tag to trigger release workflow

## Questions?

Feel free to open a discussion on GitHub!

Thank you! ❤️

