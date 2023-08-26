import os
import pytesseract
from PIL import Image
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, filename="image_text_conversion.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        logging.error(f"Error extracting text from {image_path}: {e}")
        return None

def save_text_as_md(text, output_path):
    try:
        with open(output_path, 'w') as f:
            f.write(text)
        logging.info(f"Text saved to {output_path}")
    except Exception as e:
        logging.error(f"Error saving text to {output_path}: {e}")

input_directory = "/app/screenshots"
output_directory = "/app/output_text"

logging.info("Starting image text conversion process")

image_files = [f for f in os.listdir(input_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

for image_file in image_files:
    image_path = os.path.join(input_directory, image_file)
    extracted_text = extract_text_from_image(image_path)
    if extracted_text:
        output_md_path = os.path.join(output_directory, os.path.splitext(image_file)[0] + ".md")
        save_text_as_md(extracted_text, output_md_path)

logging.info("Image text conversion process completed")
