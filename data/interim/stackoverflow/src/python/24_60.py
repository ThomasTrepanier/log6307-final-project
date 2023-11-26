def execute_multiple_prepared(conn, statements_and_values, rollback_on_error=True):
    """
    Execute multiple SQL statements and returns the cursor from the last executed statement.

    :param conn: The connection to the database
    :type conn: Database connection

    :param statements_and_values: The statements and values to be executed
    :type statements_and_values: A list of lists. Each sublist consists of a string, the SQL prepared statement with %s placeholders, and a list or tuple of its parameters

    :param: rollback_on_error: Flag to indicate action to be taken on an exception
    :type rollback_on_error: bool

    :returns cursor from the last statement executed
    :rtype cursor
    """

    try:
        cursor = conn.cursor()
        for s_v in statements_and_values:
            cursor.execute(s_v[0], s_v[1])
            if not rollback_on_error:
                conn.commit() # commit on each statement
    except Exception as e:
        if rollback_on_error:
            conn.rollback()
        raise
    else:
        if rollback_on_error:
            conn.commit() # then commit only after all statements have completed successfully
        return cursor # return the cursor in case there are results to be processed
