from flask import Flask

app = Flask(__name__)

@app.route('/test')
def test():
    return {'text': 'This is a test response from the flask backend.'}