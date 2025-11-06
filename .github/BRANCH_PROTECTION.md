# Repository Settings Guide

This document outlines the recommended GitHub repository settings for SwiftCache-SDK.

## Branch Protection Rules

To ensure code quality and prevent direct pushes to `main`, configure branch protection:

### How to Set Up (For Repository Owner)

1. Go to **Settings → Branches** in your GitHub repository
2. Click **Add rule** under "Branch protection rules"
3. Configure as follows:

```
Branch name pattern: main

✅ Require a pull request before merging
   ✅ Require approvals: 1
   ✅ Dismiss stale pull request approvals when new commits are pushed
   
✅ Require status checks to pass before merging
   (Add CI checks here once configured)
   
✅ Require conversation resolution before merging

✅ Require linear history

✅ Do not allow bypassing the above settings
   (Even admins should follow PR process)

✅ Restrict who can push to matching branches
   (Leave empty - only PRs allowed)
```

4. Click **Create** or **Save changes**

## Result

With these settings:
- ❌ **No direct pushes** to `main` (not even by owner)
- ✅ **All changes via Pull Requests**
- ✅ **Requires review approval** before merging
- ✅ **Maintains clean git history**
- ✅ **Forces discussion** on all changes

## For Contributors

Contributors should:
1. Fork the repository
2. Create feature branches in their fork
3. Submit pull requests from their fork
4. Wait for review and approval
5. Maintainer will merge after approval

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed contribution guidelines.

