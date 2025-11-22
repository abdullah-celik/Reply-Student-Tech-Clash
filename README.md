# 🕵️ PrivateEye: The Local Multimodal Analyst

> **An offline, agentic intelligence that "sees" your files and answers questions without data ever leaving your machine.**

![License](https://img.shields.io/badge/license-MIT-green) ![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![Ollama](https://img.shields.io/badge/backend-Ollama-orange) ![Status](https://img.shields.io/badge/status-Prototype-yellow)

## 💡 The Problem
Current AI tools require you to upload data to the cloud. This is a dealbreaker for:
* **Legal/Medical evidence** (Privacy laws).
* **Personal journals/photos** (Privacy concerns).
* **Remote locations** (No internet access).

Furthermore, most local RAG (Retrieval Augmented Generation) systems are **text-only**. They fail to understand charts, handwritten notes, or photographs.

## 🚀 The Solution
**PrivateEye** is a fully local, multimodal agent. It ingests mixed-media folders (images, PDFs, text), uses Vision-Language Models (VLMs) to "transcribe" visual data into semantic descriptions, and builds a searchable local knowledge graph.

### Key Capabilities
* **👁️ Visual Intelligence:** Automatically analyzes images (OCR, object detection, scene description) using `qwen2.5-vl`.
* **🔒 100% Air-Gapped:** Runs entirely on `localhost`. No API keys, no cloud usage.
* **🧠 Cross-Modal Reasoning:** Can answer questions that require combining visual evidence with textual records (e.g., *"Does the date on the receipt image match the travel log text file?"*).

---

## 🛠️ Tech Stack

* **Orchestration:** Python + LangChain/LangGraph
* **Local Inference:** [Ollama](https://ollama.com/)
* **Models:**
    * *Vision:* `qwen2.5-vl` (or `llama3.2-vision`)
    * *Reasoning:* `mistral` or `llama3`
* **Vector Database:** ChromaDB (Local persistence)
* **UI:** Streamlit

---

## ⚙️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.10+** and **Ollama** installed.

### 2. Pull Local Models
Run the following in your terminal to download the necessary weights (requires ~6GB VRAM total):
```bash
ollama pull qwen2.5-vl  # The vision model
ollama pull mistral     # The reasoning model
