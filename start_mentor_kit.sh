#!/bin/bash
# Mentor Kit — one-click launcher for the finished product.
# Opens the running Open WebUI (the AI mentor interface).
# If Open WebUI is not running, start it first.

echo "Starting Mentor Kit (Open WebUI)..."
if ! docker ps -a --format '{{.Names}}' 2>/dev/null | grep -q '^open-webui$'; then
  docker run -d \
    --name open-webui \
    -p 3000:8080 \
    -v open-webui-data:/app/backend/data \
    --add-host host.docker.internal:host-gateway \
    -e OPENAI_API_BASE_URL=http://host.docker.internal:11434/v1 \
    -e OPENAI_API_KEY=ollama \
    ghcr.io/open-webui/open-webui:main
fi
sleep 5
open http://localhost:3000
echo "Mentor Kit is ready: http://localhost:3000"
