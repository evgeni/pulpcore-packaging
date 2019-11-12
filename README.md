# pulp3 RPMs

## requirements

the scripts in this repository require the [`foreman` branch of `evgeni/pyp2rpm`](https://github.com/evgeni/pyp2rpm/tree/foreman) which contains several patches from upstream PRs

## collect dependencies

```
podman run -ti -v $(pwd):/app:Z --rm centos:7 /app/_generate_deps.sh
```

## generate

using `pyp2rpm` (latest git, 3.3.3 release has a bug with custom templates):

```
pyp2rpm -b3 -t ./_pulp3.spec -o fedora --no-autonc psycopg2 > python-psycopg2.spec
```

### all

```
./_generate_spec.sh < pulpcore-requirements.txt
```
