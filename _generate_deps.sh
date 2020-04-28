#!/bin/bash

PULPCORE_PACKAGES="pulpcore==3.2.1 pulp-file==0.2.0 pulp-container==1.2.0 pulp-rpm==3.2.0 dynaconf==3.0.0rc1"
PULPCORE_REQUIREMENTS="/app/pulpcore-requirements.txt"
FOREMAN_PACKAGING="/app/foreman-packaging"

pip3 install scikit-build
pip3 install $PULPCORE_PACKAGES
pip3 freeze |sed '/certifi/d; /gobject/d' > $PULPCORE_REQUIREMENTS

pip3 install git+https://github.com/evgeni/pyp2rpm.git@foreman#egg=pyp2rpm

if [ -d $FOREMAN_PACKAGING ]; then

  git clone --branch rpm/develop https://github.com/theforeman/foreman-packaging $FOREMAN_PACKAGING/git

  pushd $FOREMAN_PACKAGING/git

  git config --local user.email "${EMAIL:-root@localhost}"
  git config --local user.name "${NAME:-root}"
  export RPM_PACKAGER="${NAME}"

  while read line; do
    pkg=${line%==*}
    version=${line#*==}
    REWRITE_ON_SAME_VERSION=false ./add_pypi_package.sh ${pkg} ${version} katello-pulpcore-nightly-el7 pulpcore ./pyp2rpm/pulpcore.spec
  done < $PULPCORE_REQUIREMENTS

  popd
fi
