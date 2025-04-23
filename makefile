init:
	docker compose  up -d

install:
	docker compose up --build -d
	docker exec -it the-scrumfather-ollama-1 ollama pull gemma:2b

testAi :
	curl http://localhost:11434/api/generate -d '{"model": "gemma:2b","prompt": "say yes"}'

start :
	poetry run uvicorn main:app --reload

down :
	docker compose -f ./llama/docker-compose.yaml down
