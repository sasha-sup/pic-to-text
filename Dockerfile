FROM python:3.9.18-slim-bullseye
WORKDIR /app
ADD . /app
RUN useradd -m -u 1000 -s /bin/bash awesome-user \
    && chown -R awesome-user:awesome-user /app \
    && chmod -R 755 /app \
    && apt-get update \
    && apt-get install -y tesseract-ocr \
    && apt-get clean \
    && pip install -r requirements.txt \
    && mkdir screenshots output_text log
# Switch to the new user
USER awesome-user
CMD ["python", "pic-to-text.py"]
