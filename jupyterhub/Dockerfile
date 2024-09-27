FROM jupyterhub/jupyterhub:latest

# Install necessary packages
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy JupyterHub configuration
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
COPY custom/ /srv/jupyterhub/custom/

# Expose port
EXPOSE 8000

CMD ["jupyterhub"]
