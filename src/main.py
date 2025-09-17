from flask import Flask

app = Flask(__name__)


@app.route('/api/v1/details')
def hello_world():
    return 'Hello World'

# main driver function
if __name__ == '__main__':
    app.run()


# /api/v1/healthz