"""gunicorn WSGI server configuration."""
from os import environ


bind = '0.0.0.0:' + environ.get('PORT', '5000')
workers = 3

accesslog = '-'
errorlog = '-'
capture_output = True
