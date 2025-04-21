# Live Interview Bot

## Features
- **Admin‑only** upload of resumes & JDs (PDF/DOCX), assignable per candidate
- **Chat interface** with: Send, Brief, Elaborate, Regenerate, Clear, Reset, Clear All
- **AI engine** powered by Hugging Face’s open‑source Flan‑T5‑small
- **Context retrieval** via FAISS + SentenceTransformers
- **Notes** pane for quick observations
- **Free‑tier ready**: runs on CPU‑only instances (e.g. AWS/GCP free tier)

## Prerequisites
- Docker & Docker Compose (for easiest deploy)
- Or: Python 3.10+ (backend), Node 16+ (frontend)

## Quickstart with Docker
1. **Clone** this repo  
2. **Configure** backend credentials:
   ```bash
   cp backend/.env.example backend/.env
   # edit backend/.env to set ADMIN_USERNAME, ADMIN_PASSWORD, SECRET_KEY
