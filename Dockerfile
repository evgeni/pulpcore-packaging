FROM centos:7

RUN yum install -y epel-release && yum install -y postgresql-devel gcc python3 python3-devel python3-pip git git-annex rpm-build rpmdevtools crudini && yum clean all

COPY _generate_deps.sh /app/_generate_deps.sh

ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

CMD ["/bin/bash", "/app/_generate_deps.sh"]
