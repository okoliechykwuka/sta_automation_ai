from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class RequestData(BaseModel):
    test_type: str
    input_text: str

OLLAMA_SERVER_URL = "http://127.0.0.1:11434"  # Update with the Ollama server's URL

@app.get("/")
async def root():
    return {"message": "FastAPI server is running. Use POST /generate to generate test cases."}

@app.post("/generate")
async def generate(request_data: RequestData):
    try:
        prompt = f"Generate a {request_data.test_type} Robot Framework test case for: {request_data.input_text}"
        response = requests.post(
            f"{OLLAMA_SERVER_URL}/v1/completions",
            json={
                "model": "unsloth.Q4_K_M.gguf",  # Specify your model name here
                "prompt": prompt,
                "max_tokens": 500
            }
        )
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        generated_text = data['choices'][0]['text']  # Extract the generated text
        return {"generated_text": generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating test case: {str(e)}")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)