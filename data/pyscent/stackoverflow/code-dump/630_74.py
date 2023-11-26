import mysql.connector
def connection():
    conn = mysql.connector.connect(host = "XXXXX",
                  user = 'XXXXX',
                  password = 'XXXXX',
                  database = 'login_page',
                  auth_plugin='mysql_native_password')

    c = conn.cursor()
    return c , conn
