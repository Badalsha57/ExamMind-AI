# ExamMind AI 

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Framework-HuggingFace%20Transformers-orange.svg" alt="Framework">
  <img src="https://img.shields.io/badge/Model-Flan--T5--Base-red.svg" alt="AI Model">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

> **Transform Dense Documents into Structured Study Guides Instantly**

ExamMind AI is an intelligent, interactive, and production-ready educational tool designed to streamline learning workflows. The application automatically ingests heavy `.pdf` and `.docx` documents, auto-detects structural chapters/units, generates dynamic context-aware summaries, and curates customized **Question & Answer Banks** (handling both long and short forms) exported into unique, timestamped PDF packages.

---

## Architectural Flow & System Structure

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
------------------------------------------------------------------





Saving Output to a new PDF: outputs/question_bank_20260609_181530.pdf ...

PDF Generated Successfully with Answers!
Saved At: outputs/question_bank_20260609_181530.pdf
