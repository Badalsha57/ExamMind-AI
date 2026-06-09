# ExamMind AI 
> **Transform Dense Documents into Structured Study Guides Instantly**

ExamMind AI is an intelligent, interactive, and production-ready educational tool designed to streamline learning workflows. The application automatically ingests heavy `.pdf` and `.docx` documents, auto-detects structural chapters/units, generates dynamic context-aware summaries, and curates customized **Question & Answer Banks** (handling both long and short forms) exported into unique, timestamped PDF packages.

---

##  Architectural Flow & System Structure

The application architecture and internal runtime pipeline operate via the following sequence:

```text
[User Input: File Path & Q-Count] 
               │
               ▼
   [File Format Extractor] ───► (.pdf / .docx Text Extraction Layer)
               │
               ▼
     [Regex Text Cleaner] ───► (Removes junk spacing, artifacts, anomalies)
               │
               ▼
  [Smart Chapter Detector] ───► (Auto-detects Units/Headings using Regex Outlines)
               │
               ▼
 [Interactive Dropdown Menu] ───► (User selects specific chapter index target)
               │
               ▼
    [HuggingFace AI Core] ───► [Summarizer Module (Crisp Context Aggregation)]
               │          └──► [Q&A Generator Module (Flan-T5 Text-to-Text Pipeline)]
               │
               ▼
[Dynamic PDF Generation Engine] ───► (Saves unique question_bank_YYYYMMDD_HHMMSS.pdf)



<!-- Project Directory Structure -->
ExamMind-AI/
│
├── ai/
│   ├── __init__.py
│   ├── question_generator.py   # Flan-T5 conditional generation logic for Q&A pairs
│   └── summarizer.py           # Text summarization module with block handling
│
├── extractor/
│   ├── __init__.py
│   ├── pdf_extractor.py        # Core PyPDF/pypdf extraction layer
│   └── docx_extractor.py       # Docx structural layout text parser
│
├── utils/
│   ├── __init__.py
│   ├── text_cleaner.py         # Whitespace and noise token normalization utility
│   └── chapter_detector.py     # Regex matching and fallback string chunking mechanisms
│
├── pdf_generator/
│   ├── __init__.py
│   └── question_pdf.py         # ReportLab canvas styles, layouts, and compilation
│
├── outputs/                    # Auto-generated destination directory for output PDFs
├── app.py                      # Core interactive application runner (Main entry point)
└── README.md                   # Comprehensive documentation file



<!-- Coding Modules Explanation -->

1. Main Controller (app.py)
Acts as the central orchestrator of the software ecosystem. It handles initial I/O parameters, routes code pipelines dynamically based on file extensions, manages user-selected index boundaries, prints interactive terminal visuals, and maps structural list arrays into flat strings before shipping them off to the PDF generation subsystem.

2. Text Engineering (utils/)
text_cleaner.py: Scrubs raw string dumps to remove unnecessary escape delimiters, redundant double-newlines, and stray formatting artifacts while safeguarding actual word boundary tokens.

chapter_detector.py: The structural backbone of the parser. It sequentially looks for fixed history targets first. If a mismatch occurs, it unleashes a robust Regex Engine running pattern matching: (?i)(?:chapter|unit)\s+(?:\d+|[ivxlcdm]+|[a-zA-Z]+). In case of unformatted files, a fallback sequence safely splices the raw content into equal text blocks so the dropdown menu selection never surfaces empty arrays.

3. Deep Learning Inference Core (ai/)
summarizer.py: Truncates and processes localized blocks within the safety window boundaries of the model's token limits to output context overviews.

question_generator.py: Driven by HuggingFace's seq2seq google/flan-t5-base transformer model. It slices data inputs into discrete 800-character chunks to maximize context density. It passes chunks into the following structured configurations:

Question Generation Prompt: Context: {para}\n\nTask: Generate a clear question based on the context above.

Answer Extraction Prompt: Context: {para}\n\nQuestion: {q_text}\n\nTask: Answer the question precisely using the context.

Configured with optimized hyperparameters (do_sample=True, temperature=0.7, top_p=0.95) to prevent repetitive loop outputs. Contains an integrated fallback list to fill remaining target array slots if text data runs short.

4. Layout Compilation Engine (pdf_generator/)
question_pdf.py: Leverages the ReportLab flowable matrix layout framework. It splits structured strings via raw newline tokens (\n), wraps them inside flowable paragraph containers, injects typography configurations, and builds print-perfect outputs.




<!-- Live Execution Example (System Demo) -->
PS D:\exam\exam> python app.py
Enter File Path: d:\exam\exam\PYTHON PROGRAMMING NOTES.pdf
Long Questions: 3
Short Questions: 2

Reading File Contents...
Finding Chapters...

============================================================
AVAILABLE CHAPTERS
============================================================
1. UNIT I INTRODUCTION DATA, EXPRESSIONS, STATEMENTS
2. UNIT II CONTROL FLOW, LOOPS Conditionals: Boolean
3. UNIT III FUNCTIONS, ARRAYS Fruitful functions: ret
4. UNIT IV LISTS, TUPLES, DICTIONARIES Lists: list op
5. UNIT V FILES, EXCEPTIONS, MODULES, PACKAGES Files
============================================================

Select Chapter Number: 1

============================================================
SELECTED TARGET
============================================================
UNIT I INTRODUCTION DATA, EXPRESSIONS, STATEMENTS
============================================================

Creating Summary...
============================================================
SUMMARY GENERATED
============================================================
The chapter introduces the foundational paradigms of Python programming, core syntactic rules, indentation standards, interpretation mechanics, and base variable statements.
============================================================

Generating Questions & Answers...
============================================================
QUESTIONS & ANSWERS GENERATED (SERIAL NUMBER WISE)
============================================================
1. Q1. What is the fundamental role of Indentation in Python?
   Ans: Indentation in Python is used to define code blocks and scope instead of curly braces, ensuring high code readability.

2. Q2. How are variables dynamically declared in Python ecosystems?
   Ans: Variables are dynamically declared upon assignment using the assignment operator (=), without requiring explicit data type binding.

3. Q3. Explain the basic execution flow of interpreted scripting languages.
   Ans: Interpreted languages like Python process source statements line-by-line during runtime via an interpreter engine.
============================================================

Saving Output to a new PDF: outputs/question_bank_20260609_181530.pdf ...

PDF Generated Successfully with Answers!
Saved At: outputs/question_bank_20260609_181530.pdf


<!-- 2 -OutPut -->
------------------------------------------------------------------
                        EXAMMIND AI QUESTION BANK                 
------------------------------------------------------------------

Q1. What is the fundamental role of Indentation in Python?
Ans: Indentation in Python is used to define code blocks and scope instead of curly braces, ensuring high code readability.

Q2. How are variables dynamically declared in Python ecosystems?
Ans: Variables are dynamically declared upon assignment using the assignment operator (=), without requiring explicit data type binding.

Q3. Explain the basic execution flow of interpreted scripting languages.
Ans: Interpreted languages like Python process source statements line-by-line during runtime via an interpreter engine.

------------------------------------------------------------------
                     Generated automatically via ExamMind AI
------------------------------------------------------------------#   E x a m M i n d - A I 
 
 
