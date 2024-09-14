# Image Text Conversion

This Bash script automates the process of running the `pic-2-text` Docker container using Docker Compose, generating a Markdown file, and renaming it based on the content of the first line.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Image files you want to process

## Usage
 
1. Clone repository and build image:
```bash
   git clone https://github.com/sasha-sup/pic-to-text
   cd pic-to-text
   docker build -t pic2text .
```
2. Configure Volumes:
Open the docker-compose.yml file and locate the volumes.

```yaml
    volumes:
      - "YOUR/INPUT/PIC/DIRECTORY/PATH:/app/screenshots"
      - "YOUR/OUTPUT/DIRECTORY/PATH:/app/output_text"
```
3. Run app
```bash
   chmod +x app.sh
   ./app.sh
```
## What the Script Does
The script runs the pic-2-text Docker container using Docker Compose.
It waits for a moment to ensure that the container generates the .md file.

The script then extracts the first line from the generated .md file.

The first line is cleaned up to create a valid filename.

The generated .md file is renamed with the cleaned up first line as the new filename.

##  Important Note
Please review and adjust the paths and configurations in the script according to your environment and requirements before running it.