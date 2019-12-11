#!/bin/bash
yum install -y postgresql-devel gcc python3 python3-devel python3-pip
pip3 install pulpcore pulp-file pulp-container
pip3 freeze |sed '/certifi/d' > /app/pulpcore-requirements.txt
