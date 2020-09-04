#!/bin/bash

PULPCORE_PACKAGES="pulpcore==3.6.2 pulp-file==1.2.0 pulp-container==2.0.0 pulp-deb==2.6.1 pulp-rpm==3.6.1 pulp-certguard==1.0.2 galaxy-importer==0.2.8 pulp-ansible==0.2.0"
PULPCORE_REQUIREMENTS="/app/pulpcore-requirements.txt"
FOREMAN_PACKAGING="/app/foreman-packaging"

pip3 install scikit-build
pip3 install $PULPCORE_PACKAGES
pip3 freeze |sed '/gobject/d; /scikit/d; /libcomps/d; /solv/d; /createrepo/d; /distro/d; /^ansible/d' > $PULPCORE_REQUIREMENTS

pip3 install git+https://github.com/evgeni/pyp2rpm.git@foreman#egg=pyp2rpm

if [ -d $FOREMAN_PACKAGING ]; then

  git clone --branch rpm/develop https://github.com/theforeman/foreman-packaging $FOREMAN_PACKAGING/foreman
  git clone --branch rpm/3.6 https://github.com/theforeman/pulpcore-packaging $FOREMAN_PACKAGING/pulpcore

  pushd $FOREMAN_PACKAGING/pulpcore

  git config --local user.email "${EMAIL:-root@localhost}"
  git config --local user.name "${NAME:-root}"
  export RPM_PACKAGER="${NAME}"

  while read line; do
    pkg=${line%==*}
    version=${line#*==}
    REWRITE_ON_SAME_VERSION=false $FOREMAN_PACKAGING/foreman/add_pypi_package.sh ${pkg} ${version} katello-pulpcore-nightly-el7 '/' $FOREMAN_PACKAGING/foreman/pyp2rpm/pulpcore.spec
    sleep 5
  done < $PULPCORE_REQUIREMENTS

  popd
fi
