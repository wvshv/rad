from flask import Flask

app = Flask(name)

@app.route('/message', methods=['GET'])
def get_message():
    return "not implemented yet"

if name == 'main':
    app.run(port=5002)