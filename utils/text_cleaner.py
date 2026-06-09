import re

def clean_text(text):

    # Start from actual content
    keywords = [
        "Al-Biruni",
        "Ibn Battuta",
        "François Bernier",
        "Bhakti",
        "Sufi",
        "Vijayanagara",
        "Mughal"
    ]

    start_index = -1

    for keyword in keywords:

        pos = text.find(keyword)

        if pos != -1:
            start_index = pos
            break

    if start_index != -1:
        text = text[start_index:]

    text = re.sub(r'http\S+', ' ', text)
    text = re.sub(r'www\.\S+', ' ', text)

    text = re.sub(r'\s+', ' ', text)

    return text.strip()