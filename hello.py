# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#

from flask import Flask, request, jsonify


### main app
app = Flask(__name__)


### define home page ~ index.html
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        data = "http://localhost:5000/home/0"
        return jsonify({'data': data})


### define linear regression function page:
@app.route('/home/<int:x>', methods=['GET'])
def calc_y(x):
    return jsonify({'y': 25*x + 15})


if __name__ == "__main__":
    print("flask test:\n\n")
    app.run(debug=True)
