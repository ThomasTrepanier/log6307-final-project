from contextlib import closing
from typing import List

import mysql.connector
import logging

logger = logging.getLogger(__name__)


def execute(stmts: List[str]) -> None:
    logger.info("Starting daily execution")

    with closing(mysql.connector.connect()) as connection:
        try:
            with closing(connection.cursor()) as cursor:
                cursor.execute(' ; '.join(stmts), multi=True)
        except Exception:
            logger.exception("Rollbacking changes")
            connection.rollback()
            raise
        else:
            logger.info("Finished successfully")
