from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'message': 'Hello from the API!',
        'status': 'success'
    }
    return jsonify(data)

@app.route('/api/info', methods=['GET'])
def get_info():
    info = {
        'version': '1.0',
        'author': 'Alex-Austria'
    }
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)
