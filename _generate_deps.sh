#!/bin/bash

PULPCORE_PACKAGES="pulpcore pulp-file pulp-container"
PULPCORE_REQUIREMENTS="/app/pulpcore-requirements.txt"
FOREMAN_PACKAGING="/app/foreman-packaging"

pip3 install $PULPCORE_PACKAGES
pip3 freeze |sed '/certifi/d' > $PULPCORE_REQUIREMENTS

pip3 install git+https://github.com/evgeni/pyp2rpm.git@foreman#egg=pyp2rpm
pip3 install git+https://github.com/pixelb/crudini.git@0.9.3#egg=crudini

if [ -d $FOREMAN_PACKAGING ]; then
  pushd $FOREMAN_PACKAGING

  while read line; do
    pkg=${line%==*}
    version=${line#*==}
    REWRITE_ON_SAME_VERSION=false ./add_pypi_package.sh ${pkg} ${version} katello-nightly-pulpcore-el7 pulpcore ./pyp2rpm/pulpcore.spec
  done < $PULPCORE_REQUIREMENTS

  popd
fi
