# Image Text Conversion

This manual will guide you through the process of using Docker to convert images to text using the Tesseract OCR engine. The Python script extracts text from images and saves the extracted text in separate Markdown files.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Image files you want to process

## How to
 
1. Clone this repository and build image:
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
3. Run docker compose
```bash
   docker-compose up
```
