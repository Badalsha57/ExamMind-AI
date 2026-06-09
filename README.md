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
