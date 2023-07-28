install-webui:
	@cd webui && yarn install

install-webserver:
	@cd webserver && poetry install

run-webui:
	@cd webui && yarn run dev

run-webserver:
	@cd webserver && MODE=DEV uvicorn main:app --reload

build-docker:
	@docker compose --file docker/docker-compose.yml up --build

run-docker:
	@docker compose --file docker/docker-compose.yml up -d --build

upgrade:
ifndef version
	$(error The variable 'version' must be set before running this target)
endif
	@sed $(ext_sed) "s/__version__ = .*/__version__ = \"$(version)\"/" bin/sahibin
	@sed $(ext_sed) "s/version = .*/version = \"$(version)\"/" webserver/pyproject.toml
	@sed $(ext_sed) "s/\"version\": .*/\"version\": \"$(version)\",/" webui/package.json
	@sed $(ext_sed) "s/return 200 .*/return 200 \"$(version)\";/"  docker/sahibin.conf
