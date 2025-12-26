COMPOSE ?= docker compose

.PHONY: start stop status

start:
	@$(COMPOSE) up -d --build

stop:
	@$(COMPOSE) down

status:
	@$(COMPOSE) ps --format '{{.Service}}\t{{.State}}\t{{.Status}}'
