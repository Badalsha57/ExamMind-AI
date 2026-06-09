import fitz  # PyMuPDF


def extract_pdf_text(pdf_path):

    try:

        doc = fitz.open(pdf_path)

        text_parts = []

        for page_num in range(len(doc)):

            page = doc.load_page(page_num)

            page_text = page.get_text()

            if page_text.strip():
                text_parts.append(page_text)

        doc.close()

        return "\n".join(text_parts)

    except Exception as e:

        print(f"PDF Extraction Error: {e}")

        return ""