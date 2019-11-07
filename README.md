# pulp3 RPMs

## generate

using `pyp2rpm` (latest git, 3.3.3 release has a bug with custom templates):

  ```
  pyp2rpm -b3 -t ./pulp3pyp2rpm.spec -o fedora --no-autonc psycopg2 > python-psycopg2.spec
  ```
