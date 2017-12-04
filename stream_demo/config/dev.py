import os
import logging


DEPLOY = 'development'

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

SETTINGS = {
    'debug': True,
    'template_path': os.path.join(PROJECT_ROOT, 'templates'),
    'static_path': os.path.join(PROJECT_ROOT, 'static'),
    'cookie_secret': 'fhqwhgads',
    'xsrf_cookies': True
}

LOGGER_NAME = 'stream_demo'
LOGGER_LEVEL = logging.DEBUG
