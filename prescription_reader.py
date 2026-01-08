from ocr.image_preprocessor import preprocess_image
from ocr.text_extractor import extract_text
from logic.text_cleaner import clean_lines

def read_prescription(image_path):
    image = preprocess_image(image_path)
    if image is None:
        return []

    raw_text = extract_text(image)
    return clean_lines(raw_text)
