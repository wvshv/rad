from flask import Flask, request, jsonify

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(port=5001)