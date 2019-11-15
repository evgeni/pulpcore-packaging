#!/bin/bash
yum install -y postgresql-devel gcc
yum install -y python3 python3-devel python3-pip
pip3 install pulpcore pulp-file
pip3 freeze |sed 's/psycopg2-binary/psycopg2/; /certifi/d' > /app/pulpcore-requirements.txt
