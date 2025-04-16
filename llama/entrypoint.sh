#!/bin/bash

# Start Ollama in background
ollama serve &

# Wait until Ollama is ready by checking if 'ollama list' works
until ollama list > /dev/null 2>&1; do
  echo "Waiting for Ollama to start..."
  sleep 1
done

# Pull llama3 if not already present
if ! ollama list | grep -q 'llama3'; then
  echo "Pulling llama3 model..."
  ollama pull llama3
else
  echo "llama3 already pulled."
fi

# Keep it running
wait
