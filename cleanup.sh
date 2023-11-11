#!/bin/bash

# cleanup.sh

# Directories to clean
DIRS_TO_CLEAN=("build" "codespace_utils.egg-info" "__pycache__" ".pytest_cache")

echo "This script will clean up generated and temporary files."
read -p "Do you want to continue? (y/N): " confirmation

if [[ "$confirmation" != "y" && "$confirmation" != "Y" ]]; then
    echo "Cleanup canceled by the user."
    exit 1
fi

# Recursively remove __pycache__ from all directories
find . -type d -name "__pycache__" -exec rm -rf {} + \
    && echo "Removed all __pycache__ directories."

# Remove specified directories from the root of the project
for dir in "${DIRS_TO_CLEAN[@]}"; do
    if [ -d "$dir" ]; then
        rm -rf "$dir"
        echo "Removed $dir."
    else
        echo "$dir does not exist, skipping."
    fi
done

# Optionally, you can also remove *.pyc files if they're outside of __pycache__
# find . -type f -name "*.pyc" -delete

echo "Cleanup complete! Remember to regularly commit important changes to version control."
