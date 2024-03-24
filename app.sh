#!/bin/bash

set -euo pipefail
echo "Starting the script..."

# Run pic-2-text using Docker Compose
echo "Running Docker Compose..."
docker compose up -d

# Wait for a moment to ensure the container has generated the .md file
echo "Waiting for file generation..."
sleep 5

# Define the path to the local volume where files are generated
directory="/tmp"

# Loop through .md files in the directory and rename them
for file in "$directory"/*.md; do
    if [ -f "$file" ]; then
        new_filename=$(head -n 1 "$file" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' -e 's/[[:space:]]/_/g')
        mv "$file" "$directory/$new_filename.md"
        echo "Renamed: $file -> $new_filename.md"
    fi
done

echo "All files renamed."
