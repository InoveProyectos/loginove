#!/usr/bin/env python

import logging
import logging.config
from _settings import LOG_SETTINGS

logging_is_setup = False

def setup_loging(level = None):
    log_settings = LOG_SETTINGS.copy()

    if level:
        log_settings['root']['level'] = level

    logging.config.dictConfig(LOG_SETTINGS)
    global logging_is_setup
    logging_is_setup = True


def use_logging(cls):
    name = cls.__name__
    
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)
            logger = logging.getLogger(name)
            setattr(self.wrapped, 'log', logger)
        
        def __getattr__(self, name):
            return getattr(self.wrapped, name)

    return Wrapper
