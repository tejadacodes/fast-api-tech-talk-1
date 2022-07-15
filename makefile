initial-setup:
	pip3 install --upgrade pip
	pip3 install poetry
	poetry init -n
	poetry add fastapi uvicorn sqlalchemy psycopg2-binary
	mkdir .vscode
	touch .vscode/settings.json .vscode/launch.json
	cp .env.sample .env