import logging
import logging.config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'test': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
    }
}


logging.config.dictConfig(LOGGING)

l = logging.getLogger()
l.info('ROOT')

l = logging.getLogger('test')
l.info('test')
