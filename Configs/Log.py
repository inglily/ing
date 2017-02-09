# coding: utf-8
import os
import platform

PREFIX = 'E:\\MovieSpider' if platform.system() == 'Windows' \
    else '/app/python-apps-logs/MovieSpider'

# 日志文件路径
LOG_PATH_DEBUG = r'%s\debug.log' % PREFIX if platform.system() == 'Windows' else '%s/debug.log' % PREFIX
LOG_PATH_INFO = r'%s\info.log' % PREFIX if platform.system() == 'Windows' else '%s/info.log' % PREFIX
LOG_PATH_WARN = r'%s\warn.log' % PREFIX if platform.system() == 'Windows' else '%s/warn.log' % PREFIX
LOG_PATH_ERROR = r'%s\error.log' % PREFIX if platform.system() == 'Windows' else '%s/error.log' % PREFIX

# 判断目录是否存在，若不存在则创建
if not os.path.exists(PREFIX):
    os.makedirs(PREFIX)

# 是否开启流水日日志
JOUNALLOG_ENABLED = False

# 日志配置
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] %(levelname)s::(%(process)d %(thread)d)::%(module)s[line:%(lineno)d] - %(message)s'
        },
    },
    'handlers': {
        'error': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'standard',
            'filename': LOG_PATH_ERROR + '_file',
            'when': 'D',
            'interval': 1
        },
        'warn': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'WARN',
            'formatter': 'standard',
            'filename': LOG_PATH_WARN + '_file',
            'when': 'D',
            'interval': 1
        },
        'info': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'filename': LOG_PATH_INFO + '_file',
            'when': 'D',
            'interval': 1
        },
        'debug': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'filename': LOG_PATH_DEBUG + '_file',
            'when': 'D',
            'interval': 1
        }
    },
    'loggers': {
        'default': {
            'handlers': ['debug', 'info', 'warn', 'error'],
            'level': 'DEBUG',
            'propagate': True
        },
        'flask.request': {
            'handlers': ['debug', 'info', 'warn', 'error'],
            'level': 'WARN',
            'propagate': False
        },
        'tornado.application': {
            'handlers': ['debug', 'info', 'warn', 'error'],
            'level': 'WARN',
            'propagate': False
        },
        'tornado.general': {
            'handlers': ['debug', 'info', 'warn', 'error'],
            'level': 'WARN',
            'propagate': False
        }
    }
}
