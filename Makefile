install-webui:
	@cd webui && yarn install

install-webserver:
	@cd webserver && poetry install

run-webui:
	@cd webui && yarn run dev

run-webserver:
	@cd webserver && MODE=DEV uvicorn main:app --reload

build-docker:
	@docker compose up --build

run-docker:
	@docker compose up -d --build
