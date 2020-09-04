#!/bin/bash

PULPCORE_PACKAGES="pulpcore==3.6.2 pulp-file==1.2.0 pulp-container==2.0.0 pulp-deb==2.6.1 pulp-rpm==3.6.1 pulp-certguard==1.0.2 galaxy-importer==0.2.8 pulp-ansible==0.2.0"
PULPCORE_REQUIREMENTS="/app/pulpcore-requirements.txt"
PACKAGING_WORKDIR="/app/foreman-packaging"
FOREMAN_PACKAGING="${PACKAGING_WORKDIR}/foreman"
FOREMAN_PACKAGING_GIT="https://github.com/theforeman/foreman-packaging"
FOREMAN_PACKAGING_BRANCH="rpm/develop"
PULPCORE_PACKAGING="${PACKAGING_WORKDIR}/pulpcore"
PULPCORE_PACKAGING_GIT="https://github.com/theforeman/pulpcore-packaging"
PULPCORE_PACKAGING_BRANCH="rpm/3.6"
PULPCORE_TAG="katello-pulpcore-nightly-el7"

pip3 install scikit-build
pip3 install $PULPCORE_PACKAGES
pip3 freeze |sed '/gobject/d; /scikit/d; /libcomps/d; /solv/d; /createrepo/d; /distro/d; /^ansible/d' > $PULPCORE_REQUIREMENTS

pip3 install git+https://github.com/evgeni/pyp2rpm.git@foreman#egg=pyp2rpm

if [ -d $PACKAGING_WORKDIR ]; then

  git clone --branch $FOREMAN_PACKAGING_BRANCH $FOREMAN_PACKAGING_GIT $FOREMAN_PACKAGING
  git clone --branch $PULPCORE_PACKAGING_BRANCH $PULPCORE_PACKAGING_GIT $PULPCORE_PACKAGING

  pushd $PULPCORE_PACKAGING

  git config --local user.email "${EMAIL:-root@localhost}"
  git config --local user.name "${NAME:-root}"
  export RPM_PACKAGER="${NAME}"

  while read line; do
    pkg=${line%==*}
    version=${line#*==}
    REWRITE_ON_SAME_VERSION=false $FOREMAN_PACKAGING/add_pypi_package.sh ${pkg} ${version} $PULPCORE_TAG '/' $FOREMAN_PACKAGING/pyp2rpm/pulpcore.spec
    sleep 5
  done < $PULPCORE_REQUIREMENTS

  popd
fi
