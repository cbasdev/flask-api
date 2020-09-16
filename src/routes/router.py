from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/test')
def testApi():
    return jsonify({
        'test': 'success'
    })
