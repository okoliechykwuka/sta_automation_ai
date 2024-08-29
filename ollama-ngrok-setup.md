# Exposing Ollama Endpoint via ngrok

## Prerequisites!

1. Ollama installed and running
2. Fine-tuned model pulled from Hugging Face

## Setup ngrok

1. Sign up at <https://dashboard.ngrok.com/signup>
2. Download ngrok:
   - Windows: <https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip>
   - macOS: `brew install ngrok/ngrok/ngrok`
   - Linux: <https://ngrok.com/download>
3. Unzip (if downloaded as zip) and navigate to the ngrok directory in terminal

## Configure ngrok

1. Copy your authtoken from <https://dashboard.ngrok.com/get-started/your-authtoken>
2. Add the authtoken:

```bash
   ngrok config add-authtoken YOUR_AUTH_TOKEN
```

## Start Ollama

1. Open a new terminal window
2. Start Ollama server:

```bash
   ollama serve
```

## Expose Ollama via ngrok

1. In the ngrok terminal, run:

```bash
   ngrok http 11434 --host-header="localhost:11434"
```

2. Copy the generated ngrok URL (e.g., <https://xxxx-xx-xx-xxx-xx.ngrok.io>)

## Test the Connection

1. Use the ngrok URL as the base URL for your Ollama API requests
2. Example curl command:

```bash
   curl https://xxxx-xx-xx-xxx-xx.ngrok.io/api/generate -d '{"model": "YOUR_MODEL", "prompt": "Hello, world!"}'
```

## Security Considerations

- Be cautious when exposing local services to the internet
- Consider implementing authentication for your Ollama endpoint
- Monitor your ngrok dashboard for any suspicious activities

Note: The free ngrok plan has limitations. For production use, consider a paid plan or alternative solutions.
