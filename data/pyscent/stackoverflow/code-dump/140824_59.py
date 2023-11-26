def execute_multiple(conn, statements, rollback_on_error=True):
    """
    Execute multiple SQL statements and returns the cursor from the last executed statement.

    :param conn: The connection to the database
    :type conn: Database connection

    :param statements: The statements to be executed
    :type statements: A list of strings

    :param: rollback_on_error: Flag to indicate action to be taken on an exception
    :type rollback_on_error: bool

    :returns cursor from the last statement executed
    :rtype cursor
    """

    try:
        cursor = conn.cursor()
        for statement in statements:
            cursor.execute(statement)
            if not rollback_on_error:
                conn.commit() # commit on each statement
    except Exception as e:
        if rollback_on_error:
            conn.rollback()
        raise
    else:
        if rollback_on_error:
            conn.commit() # then commit only after all statements have completed successfully
