from flask import Flask


app = Flask(__name__)
REQUEST_COUNTER = 0


@app.route('/')
def hello_world():
    global REQUEST_COUNTER
    REQUEST_COUNTER += 1
    return 'Hello World!'


@app.route('/new_url/')
def new_hello_world():
    global REQUEST_COUNTER
    REQUEST_COUNTER += 1
    return {'text': 'New Hello World!', 'counter': REQUEST_COUNTER}


if __name__ == '__main__':
    app.run()
