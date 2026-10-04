# AI Marketing Copy Generator (FastAPI + Streamlit + Ollama)

A decoupled GenAI application for generating structured marketing copy and advertising campaigns powered by local Llama 3 inference.

## Architecture

The project implements a clean client-server architecture:
- **Presentation Layer (Streamlit):** Web UI capturing product metadata and telemetry.
- **Service Middleware (FastAPI):** High-performance REST API handling prompt construction, data validation with Pydantic, and response serialization.
- **Inference Engine (Ollama):** Local LLM runtime executing `llama3` for privacy-first, zero-cost completions without third-party vendor lock-in.

```text
[Streamlit UI] ---> POST /generuj ---> [FastAPI API] ---> POST /api/generate ---> [Ollama / Llama 3]
```

## Project Structure

```text
├── app.py              # Streamlit web interface
├── main.py             # FastAPI REST endpoints & LLM routing
├── requirements.txt    # Project dependencies
├── .gitignore
└── README.md
```

## Tech Stack

- **Backend:** FastAPI, Pydantic, Uvicorn
- **Frontend:** Streamlit
- **Model Runtime:** Ollama (Meta Llama 3)
- **Networking:** Requests (HTTP Client)

## Setup & Local Execution

### Prerequisites

Ensure [Ollama](https://ollama.com/) is installed and running with Llama 3 pulled:
```bash
ollama run llama3
```

### Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/wiktoria215/AI-Marketing-Tool.git](https://github.com/wiktoria215/AI-Marketing-Tool.git)
   cd AI-Marketing-Tool
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Services

1. Start the FastAPI backend:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

2. In a separate terminal, launch the Streamlit interface:
   ```bash
   streamlit run app.py
   ```