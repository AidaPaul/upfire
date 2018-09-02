from evennia.settings_default import *

# This is the name of your game. Make it catchy!
SERVERNAME = "upfire"

# Telnet ports. Visible.
TELNET_ENABLED = True
TELNET_PORTS = [4000]
# (proxy, internal). Only proxy should be visible.
WEBSERVER_ENABLED = True
WEBSERVER_PORTS = [(4001, 4002)]
# Telnet+SSL ports, for supporting clients. Visible.
SSL_ENABLED = False
SSL_PORTS = [4003]
# SSH client ports. Requires crypto lib. Visible.
SSH_ENABLED = False
SSH_PORTS = [4004]
# Websocket-client port. Visible.
WEBSOCKET_CLIENT_ENABLED = True
WEBSOCKET_CLIENT_PORT = 4005
# Internal Server-Portal port. Not visible.
AMP_PORT = 4006

INSTALLED_APPS = INSTALLED_APPS + ('raven.contrib.django.raven_compat',)

try:
    from server.conf.secret_settings import *
except ImportError:
    print "secret_settings.py file not found or failed to import."
