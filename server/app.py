from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import uuid, json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/api/todolist', methods=['GET'])
def ping_pong():
    rst = make_response(json.dumps(["test", "Del"]))
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3001)