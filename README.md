# pulp3 RPMs

## collect dependencies

```
podman run -ti -v $(pwd):/app:Z --rm centos:7 /app/_generate_deps.sh
```

## generate

using `pyp2rpm` (latest git, 3.3.3 release has a bug with custom templates):

  ```
  pyp2rpm -b3 -t ./pulp3pyp2rpm.spec -o fedora --no-autonc psycopg2 > python-psycopg2.spec
  ```

### all

  ```
  ./_generate_spec.sh < pulpcore-requirements.txt
  ```
