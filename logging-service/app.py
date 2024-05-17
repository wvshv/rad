from flask import Flask, request, jsonify

app = Flask(name)

messages = {}

@app.route('/log', methods=['POST'])
def log_message():
    data = request.json
    messages[data['UUID']] = data['msg']
    return jsonify({"status": "logged"}), 200

@app.route('/log', methods=['GET'])
def get_messages():
    all_messages = "\n".join(messages.values())
    return all_messages

if name == 'main':
    app.run(port=5001)