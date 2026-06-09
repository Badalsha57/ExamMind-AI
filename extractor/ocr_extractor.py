import easyocr
import os


# Reader sirf ek baar load hoga
reader = easyocr.Reader(
    ['en'],
    gpu=False
)


def extract_ocr_text(image_path):

    try:

        if not os.path.exists(image_path):

            print(
                f"File not found: {image_path}"
            )

            return ""

        result = reader.readtext(
            image_path,
            detail=0,
            paragraph=True
        )

        text = " ".join(result)

        return text.strip()

    except Exception as e:

        print(
            f"OCR Error: {e}"
        )

        return ""