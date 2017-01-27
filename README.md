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

## Backup/restore

This doesn't work :(

```console
$ docker-compose exec postgres \
	pg_dump -Upostgres --clean --format=tar postgres >backup.tar
```

```console
$ docker-compose exec postgres \
	pg_restore -Upostgres --format=tar --dbname=postgres <backup.tar
```
