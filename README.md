# Dockerised bitsbox

```console
$ pip install -r requirements.txt
$ docker-compose build
$ docker-compose up -d
$ docker-compose exec web ./runflask.sh db upgrade
```

Optionally:

```console
$ docker-compose exec web ./runflask.sh bitsbox importlayouts layouts.yaml
```

## Secrets

Vsrious secrets such as passwords, etc are stored in the ``secrets-env`` file.
An example is provided but one may be generated via gen_secrets.py which also
configures the user for basic auth over web.

## Backup/restore

Dump datavase from

```console
$ docker-compose exec postgres pg_dump -Ubitsbox -c >backup.sql
```

Restore using local psql client

```console
$ psql -h $(docker-machine ip) -Ubitsbox -f backup.sql bitsbox
```
