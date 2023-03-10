#! /bin/bash
docker image build -t umer2001/django-movies:latest .
docker images
docker push umer2001/django-movies:latest
