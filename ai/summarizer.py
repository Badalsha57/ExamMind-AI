from transformers import pipeline, AutoTokenizer
import re

MODEL = "google/flan-t5-base"

summarizer = pipeline(
    "text2text-generation",
    model=MODEL
)

tokenizer = AutoTokenizer.from_pretrained(MODEL)


def summarize_text(text):

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove very common NCERT front-page garbage
    remove_words = [
        "First Edition",
        "Reprinted",
        "Published at",
        "NCERT",
        "ISBN",
        "Printed on",
        "National Council of Educational Research and Training",
        "Notes",
        "Fig.",
        "Map work"
    ]

    for word in remove_words:
        text = text.replace(word, "")

    # Keep only first useful part
    text = text[:5000]

    words = text.split()

    chunks = []
    current_chunk = []

    for word in words:

        current_chunk.append(word)

        chunk_text = " ".join(current_chunk)

        tokens = tokenizer.encode(
            chunk_text,
            add_special_tokens=False
        )

        if len(tokens) > 450:

            current_chunk.pop()

            chunks.append(
                " ".join(current_chunk)
            )

            current_chunk = [word]

    if current_chunk:
        chunks.append(
            " ".join(current_chunk)
        )

    summaries = []

    for i, chunk in enumerate(chunks):

        print(f"Summarizing chunk {i+1}/{len(chunks)}")

        prompt = f"""
Summarize the important historical concepts, events, people and ideas from the chapter.

Chapter Text:
{chunk}

Summary:
"""

        result = summarizer(
            prompt,
            max_new_tokens=120,
            truncation=True
        )

        summaries.append(
            result[0]["generated_text"]
        )

    final_summary = "\n".join(summaries)

    return final_summary