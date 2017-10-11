from flask import Flask, request, jsonify
from blueiris import BlueIris
import json
import os
app = Flask(__name__)

host = '{}:{}'.format(os.environ['BI_HOST'], os.environ['BI_PORT'])
user = os.environ['BI_USER']
password = os.environ['BI_PASSWORD']

@app.route("/signal", methods=['GET'])
def get_signal():
    blueIris = BlueIris(host, user, password, debug=True)
    return jsonify({'signal': blueIris.get_signal()})
@app.route("/signal", methods=['POST'])
def set_signal():
    blueIris = BlueIris(host, user, password, debug=True)
    data = request.get_data()
    body = json.loads(data)
    signal = body['signal']
    blueIris.set_signal(signal)
    return get_signal()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)