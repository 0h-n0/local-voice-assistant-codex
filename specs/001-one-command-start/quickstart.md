# Quickstart: One-Command Service Startup

## Start

```sh
make start
```

Expected: backend and frontend services start; compose output indicates running
containers.

## Status

```sh
make status
```

Expected: service status output lists each service and its state.

## Stop

```sh
make stop
```

Expected: services stop cleanly without errors.

## Notes

- Uses docker-compose via the Makefile wrapper.
