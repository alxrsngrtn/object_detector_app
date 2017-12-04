import logging
import tornado.util
from tornado.options import define, options


define('env', default='dev')
define('port', default=8888)
options.parse_command_line()

if options.env == 'dev':
    config = tornado.util.import_object('config.dev')


def create_log():
    logger = logging.getLogger(config.LOGGER_NAME)
    logger.setLevel(config.LOGGER_LEVEL)
    return logger


logger = create_log()
logger.info('settings initialized.')
