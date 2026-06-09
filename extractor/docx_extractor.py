from docx import Document


def extract_docx_text(docx_path):

    try:

        doc = Document(docx_path)

        text = []

        for para in doc.paragraphs:

            if para.text.strip():
                text.append(para.text)

        return "\n".join(text)

    except Exception as e:

        print(f"DOCX Extraction Error: {e}")

        return ""