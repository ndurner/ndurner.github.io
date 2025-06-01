#!/bin/bash

# Create hooks directory if it doesn't exist
mkdir -p .git/hooks

# Install post-commit hook
cp "$(git rev-parse --show-toplevel)/scripts/.hooks/post-commit" .git/hooks/
chmod +x .git/hooks/post-commit

echo "Git hooks installed successfully!"
