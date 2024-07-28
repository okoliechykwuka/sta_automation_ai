# Setup

## Running Ollama Server

- Install Ollama:

```bash
curl https://ollama.ai/install.sh | sh
```

- Create a Modelfile:
Modelfile has already been created..., can be found in `src/app/`

- Build and Run the Model with Ollama:

```bash
ollama create unsloth.Q4_K_M.gguf -f Modelfile
```

---

## Setting Up the FastAPI Server

### Install Dependencies

```bash
pip install fastapi uvicorn
```