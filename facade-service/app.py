from flask import Flask, request, jsonify 
import requests
import uuid 

app = Flask{__name__}

LOGGIN_SERVICE_URL ='http://localhost:5001/log'
MESSAGES_SERVICE_URL ='http://localhost:5002/message'

@app.route('/msg', methods=['POST'])
def post_message():
    msg = request.json.get('msg')
    message_id = str(uuid.uuid4())
    data = {'UUID': message_id, 'msg': msg}
    response = requests.post(LOGGING_SERVICE_URL, json=data)
    return jsonify(response.json()), response.status_code

@app.route('/msg', methods=['GET'])
def get_messages():
    log_response = requests.get(LOGGING_SERVICE_URL)
    msg_response = requests.get(MESSAGES_SERVICE_URL)
    all_messages = log_response.text + "\n" + msg_response.text
    return all_messages

if name == 'main':
    app.run(port=5000)