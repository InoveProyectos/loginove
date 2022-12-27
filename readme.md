# loginove

## Cómo integrar el visualizador de logs en una aplicación usando Docker
En `docker-compose.yml`
```docker
services:
    ...
    log_viewer:
        image: juliansalinas20/log-viewer:first-tag
        expose:
            - "8111"

        ports:
        - "8111:8111"

        volumes:
        - <tus-logs>:/app
```