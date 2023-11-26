def logger(filename, level=None, format=None):
    """A wrapper to the logging python module

    This module is useful for cases where we need to log in a for loop
    different files. It also will allow more flexibility later on how the
    logging format could evolve.

    Parameters
    ----------
    filename : str
        Name of logfile. 
    level : str, optional
        Level of logging messages, by default 'info'. Supported are: 'info'
        and 'debug'.
    format : str, optional
        Format of logging messages, by default '%(message)s'.

    Returns
    -------
    logger
        A logger object.
    """

    levels = {"info": logging.INFO, "debug": logging.DEBUG}

    if level is None:
        level = levels["info"]
    else:
        level = levels[level.lower()]

    if format is None:
        format = "%(message)s"

    # https://stackoverflow.com/a/12158233/1995261
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logger = logging.basicConfig(filename=filename, level=level, format=format)

    return logger
