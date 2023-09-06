#!/bin/bash

#####################################################
# README:
# 
# Before running this script, make sure to change the 
# local_volume_path to the correct directory path where 
# files are generated and path to docker compose file
#####################################################

#!/bin/bash
set -euo pipefail
set +x
echo "Starting the script..."

# Run pic-2-text using Docker Compose
echo "Running Docker Compose..."
docker compose -f your/path/to/docker-compose.yml up -d

# Wait for a moment to ensure the container has generated the .md file
echo "Waiting for file generation..."
sleep 5

# Define the path to the local volume where files are generated
directory="YOUR/OUTPUT/DIRECTORY/PATH"

# Loop through .md files in the directory and rename them
for file in "$directory"/*.md; do
    if [ -f "$file" ]; then
        new_filename=$(head -n 1 "$file" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' -e 's/[[:space:]]/_/g')
        mv "$file" "$directory/$new_filename.md"
        echo "Renamed: $file -> $new_filename.md"
    fi
done

echo "All files renamed."
