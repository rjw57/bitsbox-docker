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

