FROM python:3.9.18-slim-bullseye
WORKDIR /app
ADD . /app
RUN apt-get update \
    && apt-get install -y tesseract-ocr \
    && apt-get clean \
    && pip install -r requirements.txt \
    && mkdir screenshots output_text
CMD ["python", "pic-to-text.py"]
