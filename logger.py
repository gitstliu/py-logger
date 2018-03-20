import logging.handlers

class Logger:
    logger = None

    log_level = logging.DEBUG
    log_file = "sa.log"
    log_max_byte = 100 * 1024 * 1024;
    log_backup_count = 10

    @staticmethod
    def getLogger():
        if Logger.logger is not None:
            return Logger.logger

        Logger.logger = logging.Logger("Logger")
        log_handler = logging.handlers.RotatingFileHandler(filename=Logger.log_file, \
                                                           maxBytes=Logger.log_max_byte, \
                                                           backupCount=Logger.log_backup_count)
        log_fmt = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
        log_handler.setFormatter(log_fmt)
        Logger.logger.addHandler(log_handler)
        Logger.logger.setLevel(Logger.log_level)
        return Logger.logger

log = Logger.getLogger()