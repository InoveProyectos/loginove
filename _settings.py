LOG_SETTINGS = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
      "simple": {
        "format": "%(asctime)s.%(msecs)03d | %(levelname)s | [%(filename)s] | [%(lineno)d] | %(message)s",
        "datefmt": "%Y-%m-%dT%H:%M:%S"
      }
    },
  
    "handlers": {
      "console": {
        "class": "logging.StreamHandler",
        "level": "DEBUG",
        "formatter": "simple",
        "stream": "ext://sys.stdout"
      },
  
      "info_file_handler": {
        "class": "logging.handlers.RotatingFileHandler",
        "level": "INFO",
        "formatter": "simple",
        "filename": "logs/info.log",
        "maxBytes": 10485760,
        "backupCount": 5,
        "encoding": "utf8"
      },
  
      "error_file_handler": {
        "class": "logging.handlers.RotatingFileHandler",
        "level": "ERROR",
        "formatter": "simple",
        "filename": "logs/errors.log",
        "maxBytes": 10485760,
        "backupCount": 5,
        "encoding": "utf8"
      }
    },
  
 
    "root": {
      "level": "INFO",
      "handlers": ["console", "info_file_handler", "error_file_handler"]
    }
  }