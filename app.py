import os
from datetime import datetime  # Timestamp ke liye top par import kiya

from extractor.pdf_extractor import (
    extract_pdf_text
)
from extractor.docx_extractor import (
    extract_docx_text
)
from utils.text_cleaner import (
    clean_text
)
from utils.chapter_detector import (
    find_chapters
)
from ai.summarizer import (
    summarize_text
)
from ai.question_generator import (
    generate_questions
)
from pdf_generator.question_pdf import (
    generate_pdf
)


def process_file():

    file_path = input(
        "Enter File Path: "
    )

    long_q = int(
        input(
            "Long Questions: "
        )
    )

    short_q = int(
        input(
            "Short Questions: "
        )
    )

    ext = os.path.splitext(
        file_path
    )[1].lower()

    # Extract Text
    if ext == ".pdf":

        text = extract_pdf_text(
            file_path
        )

    elif ext == ".docx":

        text = extract_docx_text(
            file_path
        )

    else:

        print(
            "Unsupported File"
        )
        return

    # Clean Text
    text = clean_text(text)

    print(
        "\nFinding Chapters..."
    )

    chapters = find_chapters(text)

    if len(chapters) == 0:

        print(
            "\nNo chapters found."
        )
        return

    print("\n" + "=" * 60)
    print("AVAILABLE CHAPTERS")
    print("=" * 60)

    for i, chapter in enumerate(
        chapters,
        start=1
    ):

        print(
            f"{i}. {chapter['title'][:100]}"
        )

    print("=" * 60)

    choice = int(
        input(
            "\nSelect Chapter Number: "
        )
    )

    if choice < 1 or choice > len(chapters):

        print(
            "Invalid Chapter Number"
        )
        return

    selected_text = chapters[
        choice - 1
    ]["text"]

    print("\n" + "=" * 60)
    print("SELECTED CHAPTER")
    print("=" * 60)
    print(chapters[choice - 1]["title"])
    print("=" * 60)

    print(
        "\nCreating Summary..."
    )

    # Token limit crash se bachne ke liye safe text chunk size pass kiya
    summary = summarize_text(
        selected_text[:4000]
    )

    print("\n" + "=" * 60)
    print("SUMMARY GENERATED")
    print("=" * 60)
    print(summary)
    print("=" * 60)

    print(
        "\nGenerating Questions..."
    )

    questions = generate_questions(
        selected_text[:5000],
        long_q,
        short_q
    )

    print("\n" + "=" * 60)
    print("QUESTIONS GENERATED (SERIAL NUMBER WISE)")
    print("=" * 60)
    
    # List ke har question ko serial number ke saath terminal par dikhane ke liye
    for i, q in enumerate(questions, start=1):
        print(f"{i}. {q}")
        
    print("=" * 60)

    # --- DYNAMIC TIMESTAMP PDF GENERATION BLOCK ---
    
    # 1. Har question ke aage serial number jodein taaki PDF me number dikhe
    questions_with_sl_no = []
    for i, q in enumerate(questions, start=1):
        questions_with_sl_no.append(f"{i}. {q}")
    
    pdf_data_string = "\n".join(questions_with_sl_no)

    # 2. Output folder check/create karna
    os.makedirs(
        "outputs",
        exist_ok=True
    )
    
    # 3. Dynamic aur Unique File Name banana timestamp ke saath (Format: YYYYMMDD_HHMMSS)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_pdf_path = f"outputs/question_bank_{timestamp}.pdf"

    # 4. PDF me formatted string pass karein aur save karein
    print(f"\nSaving Output to a new PDF: {output_pdf_path} ...")
    try:
        generate_pdf(pdf_data_string, output_pdf_path)
        print("\nPDF Generated Successfully!")
        print(f"Saved At: {output_pdf_path}")
    except Exception as e:
        print(f"\nPDF Generation Failed: {e}")


if __name__ == "__main__":

    process_file()