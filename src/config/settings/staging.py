DEBUG = False

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
]
CORS_REPLACE_HTTPS_REFERER = True
CSRF_COOKIE_DOMAIN = ''
CORS_ORIGIN_WHITELIST = tuple(
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'color',
        },
        'tempfile': {
            'class': 'logging.FileHandler',
            'filename': '/tmp/django.log',
            'mode': 'a',
            'level': 'DEBUG',
            'formatter': 'plain'
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'config': {
            'handlers': ['console', 'tempfile'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propogate': False,
        },
    },
    'formatters': {
        'plain': {
            "format": "%(asctime)-22s [%(process)d] %(name)-30s %(lineno)-5d %(levelname)-8s %(message)s"
        },
        'color': {
            "()": "colorlog.ColoredFormatter",
            "format": "%(log_color)s%(asctime)-22s [%(process)d] %(name)-30s %(lineno)-5d %(levelname)-8s %(message)s",
        }
    }
}
