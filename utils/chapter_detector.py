import re

def find_chapters(text):
    # 1. Hardcoded History Chapter Names (Aapki original list)
    history_chapters = [
        "Through the Eyes of Travellers",
        "Bhakti-Sufi Traditions",
        "An Imperial Capital",
        "Peasants, Zamindars and the State",
        "Kings and Chronicles"
    ]

    chapters = []
    positions = []

    # Step A: Pehle aapki di gayi History list ko dhoondhein
    for chapter in history_chapters:
        pos = text.lower().find(chapter.lower())
        if pos != -1:
            positions.append((pos, chapter))

    # Step B: Agar History chapters nahi mile, toh smart Regex use karein (For Python Notes/Other PDFs)
    if not positions:
        # Yeh pattern dhoondhega: "Chapter 1", "Unit I", "1. Introduction", "CHAPTER ONE" etc.
        regex_pattern = r'(?i)(?:chapter|unit)\s+(?:\d+|[ivxlcdm]+|[a-zA-Z]+)|\b\d+\.\s+[A-Z][a-zA-Z\s]{3,}'
        matches = list(re.finditer(regex_pattern, text))
        
        for match in matches:
            pos = match.start()
            # Poori line ko title banane ke liye '\n' tak ka text nikalenge
            line_end = text.find('\n', pos)
            if line_end == -1:
                line_end = pos + 50
            title = text[pos:line_end].strip()
            
            # Kuch khali ya choti lines ko filter karne ke liye
            if len(title) > 3 and (pos, title) not in positions:
                positions.append((pos, title))

    # Step C: FALLBACK - Agar regex se bhi kuch na mile, toh text ko chunking parts me baant do
    if not positions:
        # File badi hoti hai toh hum use automatically 4 parts me divide kar dete hain
        chunk_size = max(1, len(text) // 4)
        for i in range(4):
            start_pos = i * chunk_size
            if start_pos < len(text):
                positions.append((start_pos, f"Section Part {i+1} (Auto Generated Block)"))

    # Positions ko sort karein (Aapka original logic)
    positions.sort()

    # Text ko split karke chapters dictionary banane ka aapka original loop
    for i in range(len(positions)):
        start = positions[i][0]

        if i < len(positions) - 1:
            end = positions[i + 1][0]
        else:
            end = len(text)

        chapter_text = text[start:end].strip()

        chapters.append(
            {
                "title": positions[i][1],
                "text": chapter_text
            }
        )

    return chapters