from flask import Flask, jsonify

from database.database import Connection
from psycopg2 import sql, extras


app = Flask(__name__)


@app.route('/test')
def testApi():
    conn = Connection().conn
    query = sql.SQL(
        """
            SELECT * FROM users;
        """
    )

    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    conn.close()

    print("QUERY --> ", data)
    return jsonify({
        'test': 'success',
        'body': 'prueba'
    })
