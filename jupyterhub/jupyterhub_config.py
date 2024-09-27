import os
from oauthenticator.generic import GenericOAuthenticator

c = get_config()

# Spawn containers using DockerSpawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# DockerSpawner configuration
c.DockerSpawner.image = 'kkcluster/singleuser:latest'
c.DockerSpawner.remove = True  # Remove containers when they stop

# Network settings
c.JupyterHub.hub_ip = 'jupyterhub'
c.JupyterHub.hub_port = 8000

# OAuth configuration
c.JupyterHub.authenticator_class = GenericOAuthenticator
c.GenericOAuthenticator.client_id = os.environ['OAUTH_CLIENT_ID']
c.GenericOAuthenticator.client_secret = os.environ['OAUTH_CLIENT_SECRET']
c.GenericOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']
c.GenericOAuthenticator.authorize_url = 'https://your-auth-server.com/oauth/authorize'
c.GenericOAuthenticator.token_url = 'https://your-auth-server.com/oauth/token'
c.GenericOAuthenticator.userdata_url = 'https://your-auth-server.com/api/userinfo'
c.GenericOAuthenticator.userdata_method = 'GET'
c.GenericOAuthenticator.username_key = 'preferred_username'

c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '2G'

# SSL settings (if applicable)
# c.JupyterHub.ssl_cert = '/path/to/ssl/cert'
# c.JupyterHub.ssl_key = '/path/to/ssl/key'
