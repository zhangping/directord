
import logging
import logging.config
import logging.handlers

LOG_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
                'standard': {
                        'format': '%(asctime)s %(name)s %(module)s.%(funcName)s %(levelname)s %(message)s'
                },
                'accessrecord': {
                        'format': '%(asctime)s %(message)s'
                }
        },
        'filters': {
                'root': {
                'name': 'root',
                }
        },
        'handlers': {
                'console': {
                        'level': 'DEBUG',
                        'class': 'logging.StreamHandler',
                        'formatter': 'standard',
                        'stream': 'ext://sys.stdout',
                },
	        'directord': {
                        'level': 'DEBUG',
                        'class': 'logging.handlers.RotatingFileHandler',
                        'formatter': 'standard',
                        'filename': '/var/log/directord.log',
                        'mode': 'a',
                        'maxBytes': 10485760,
                        'backupCount': 6,
                },
	        'access': {
                        'level': 'DEBUG',
                        'class': 'logging.handlers.TimedRotatingFileHandler',
                        'when': 'm',
                        'interval': 5,
                        'formatter': 'accessrecord',
                        'filename': '/var/log/access.log',
                        'backupCount': 6,
                },
        },
        'loggers': {
                'access': {
                        'handlers': ['access'],
                        'level': 'DEBUG'
                }
        },
        'root': {
                'handlers': ['directord'],
                'level': 'DEBUG',
                'filters': ['root']
        }
}

if __name__ == '__main__':
        try:
                logging.config.dictConfig (LOG_CONFIG)
        except ValueError:
                print "value error"
        except TypeError:
                print "type error"
        except AttributeError:
                print "attribute error"
        else:
                print "logging config success"
        logger = logging.getLogger ()
        logger.debug ("hhhhhhhhhhhhhhhhhhhhhh")
        logger.info ("hhhhhhhhhhhhhhhhhhhhhh")
        logger.warning ("hhhhhhhhhhhhhhhhhhhhhh")
        logger.error ("hhhhhhhhhhhhhhhhhhhhhh")
        logger.critical ("hhhhhhhhhhhhhhhhhhhhhh")
        logger = logging.getLogger ("access")
        logger.debug ("hhhhhhhhhhhhhhhhhhhhhh")
        logger.info ("hhhhhhhhhhhhhhhhhhhhhh")
        logger.warning ("hhhhhhhhhhhhhhhhhhhhhh")
        logger.error ("hhhhhhhhhhhhhhhhhhhhhh")
        logger.critical ("hhhhhhhhhhhhhhhhhhhhhh")
