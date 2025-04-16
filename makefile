initAi :
	docker compose -f ./llama/docker-compose.yaml up -d

installAi :
	docker compose -f ./llama/docker-compose.yaml up -d
	docker exec -it llama-ollama-1 ollama pull gemma:2b

testAi :
	curl http://localhost:11434/api/generate -d '{"model": "gemma:2b","prompt": "say yes"}'

start :
	poetry run python main.py

down :
	docker compose -f ./llama/docker-compose.yaml down
