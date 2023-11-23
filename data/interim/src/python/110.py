def redirect_werkzeug_logs_to_loguru(record):
    log_level = logging.getLevelName(record.levelno)
    logger_opt = logger.opt(depth=6, exception=record.exc_info)
    logger_opt.log(log_level, record.getMessage())
