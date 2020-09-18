from psycopg2 import connect, sql


class Connection:
    def __init__(self):
        self.conn = connect(
            database='tecspense',
            user='postgres',
            password='password',
            host='localhost',
            port=5432
        )
        self.schema = sql.Identifier('private')

    def close(self):
        self.conn.close()
