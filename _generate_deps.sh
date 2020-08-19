#!/bin/bash

PULPCORE_PACKAGES="pulpcore==3.4.1 pulp-file==1.0.1 pulp-container==1.4.2 pulp-rpm==3.5.0 dynaconf==3.0.0 pulp-certguard==0.1.0rc5 galaxy-importer==0.2.8rc9 pulp-ansible==0.2.0b15 galaxy_ng==4.2.0a12"
PULPCORE_REQUIREMENTS="/app/pulpcore-requirements.txt"
FOREMAN_PACKAGING="/app/foreman-packaging"

pip3 install scikit-build
pip3 install $PULPCORE_PACKAGES
pip3 freeze |sed '/gobject/d; /scikit/d; /libcomps/d; /solv/d; /createrepo/d; /distro/d' > $PULPCORE_REQUIREMENTS

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
