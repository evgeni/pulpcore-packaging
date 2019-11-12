#!/bin/bash

PYP2RPM=pyp2rpm
TEMPLATE=./pulp3pyp2rpm.spec

while read line; do
  pkg=$(echo ${line} |cut -f1 -d=)
  pkg_lower=$(echo ${pkg} |tr '[A-Z]' '[a-z]')
  version=$(echo ${line} | cut -f3 -d=)
  if [[ $pkg != $pkg_lower ]]; then
    rpm_name_arg="-r python-${pkg_lower}"
  else
    rpm_name_arg=""
  fi
  $PYP2RPM -b3 -t $TEMPLATE -o fedora --no-autonc --skip-check --no-include-extras -v ${version} ${rpm_name_arg} ${pkg} > python-${pkg_lower}.spec
  sed -i '/sphinx/d' python-${pkg_lower}.spec
done
