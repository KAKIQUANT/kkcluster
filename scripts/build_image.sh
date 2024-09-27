#!/bin/bash

# Build JupyterHub image
docker build -t kkcluster/jupyterhub:latest ./jupyterhub

# Build single-user notebook image
docker build -t kkcluster/singleuser:latest ./singleuser

# Build NGINX image
docker build -t kkcluster/nginx:latest ./nginx
