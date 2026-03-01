import logging
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import pytesseract
from PIL import Image, UnidentifiedImageError

LOGGER = logging.getLogger(__name__)
SUPPORTED_EXTENSIONS = (".png", ".jpg", ".jpeg")


@dataclass(frozen=True)
class Settings:
    input_directory: Path
    output_directory: Path

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            input_directory=Path(os.getenv("INPUT_DIRECTORY", "/app/screenshots")),
            output_directory=Path(os.getenv("OUTPUT_DIRECTORY", "/app/output_text")),
        )


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
        force=True,
    )


def extract_text_from_image(image_path: Path) -> Optional[str]:
    try:
        with Image.open(image_path) as image:
            return pytesseract.image_to_string(image)
    except (UnidentifiedImageError, OSError, pytesseract.TesseractError) as error:
        LOGGER.error("Error extracting text from %s: %s", image_path, error)
        return None


def save_text_as_md(text: str, output_path: Path) -> bool:
    try:
        output_path.write_text(text, encoding="utf-8")
        LOGGER.info("Text saved to %s", output_path)
        return True
    except OSError as error:
        LOGGER.error("Error saving text to %s: %s", output_path, error)
        return False


def iter_image_files(input_directory: Path) -> list[Path]:
    return sorted(
        path
        for path in input_directory.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    )


def process_images(settings: Settings) -> int:
    if not settings.input_directory.is_dir():
        LOGGER.error("Input directory does not exist: %s", settings.input_directory)
        return 1

    settings.output_directory.mkdir(parents=True, exist_ok=True)
    image_files = iter_image_files(settings.input_directory)
    LOGGER.info("Found %s image(s) for processing", len(image_files))

    converted_files = 0
    for image_path in image_files:
        extracted_text = extract_text_from_image(image_path)
        if not extracted_text:
            continue

        output_md_path = settings.output_directory / f"{image_path.stem}.md"
        if save_text_as_md(extracted_text, output_md_path):
            converted_files += 1

    LOGGER.info(
        "Image text conversion process completed: %s/%s file(s) saved",
        converted_files,
        len(image_files),
    )
    return 0


def main() -> int:
    configure_logging()
    LOGGER.info("Starting image text conversion process")
    settings = Settings.from_env()
    return process_images(settings)


if __name__ == "__main__":
    raise SystemExit(main())
