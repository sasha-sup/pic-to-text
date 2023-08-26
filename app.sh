#!/bin/bash

#####################################################
# README:
# 
# Before running this script, make sure to change the 
# local_volume_path to the correct directory path where 
# files are generated and path to docker compose file
#####################################################

echo "Starting the script..."

# Run pic-2-text using Docker Compose
echo "Running Docker Compose..."
# Run pic-2-text
docker compose -f /home/sasha/code/personal-projects/pic-to-text/docker-compose.yml up -d

# Wait for a moment to ensure the container has generated the .md file
echo "Waiting for file generation..."
sleep 5

# Define the path to the local volume where files are generated
local_volume_path="/home/sasha/code/studies/aws/cloud-practitioner-CLF-C01-CLF-C02/output_text"

# Get the name of the generated .md file
generated_file=$(ls "$local_volume_path"/*.md)

# Extract the first line from the generated file
first_line=$(head -n 1 "$generated_file")

# Remove any unwanted characters from the first line to create a valid filename
new_filename=$(echo "$first_line" | tr -d '\n\r' | tr -d '/\?<>:*|"')

# Rename the generated file with the new filename
mv "$generated_file" "$local_volume_path/$new_filename.md"
echo "File renamed to: $new_filename.md"
