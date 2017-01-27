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

Dump datavase from

```console
$ docker-compose exec postgres \
	pg_dumpall -Upostgres --clean >backup.sql
```

Restore using local psql client

```console
$ psql -h $(docker-machine ip) -U postgres -f backup.sql
```
