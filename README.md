# pulp3 RPMs

## generate

using `pyp2rpm` (latest git, 3.3.3 release has a bug with custom templates):

  ```
  pyp2rpm -b3 -t ./pulp3pyp2rpm.spec -o fedora --no-autonc psycopg2 > python-psycopg2.spec
  ```

### all

  ```
  while read line; do pkg=$(echo ${line} |cut -f1 -d=); version=$(echo ${line} | cut -f3 -d=); pyp2rpm -b3 -t ./pulp3pyp2rpm.spec -o fedora --no-autonc -v ${version} ${pkg} > python-${pkg}.spec; done < pulpcore-requirements.txt
  ```
