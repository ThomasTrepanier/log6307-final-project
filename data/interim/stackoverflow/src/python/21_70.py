import logging

import click
    

class RemoveColorFilter(logging.Filter):
    def filter(self, record):
        if record and record.msg and isinstance(record.msg, str):
            record.msg = click.unstyle(record.msg) 
        return True

remove_color_filter = RemoveColorFilter()
file_handler_access_log.addFilter(remove_color_filter)
