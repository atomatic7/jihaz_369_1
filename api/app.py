from flask import Flask, request, jsonify, render_template
from chat import add_message, get_messages  # Import functions from chat.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    username = data.get('username')
    message = data.get('message')
    if not username or not message:
        return jsonify({'error': 'Both username and message are required!'}), 400

    add_message(username, message)  # Call function from chat.py
    return jsonify({'success': True, 'message': 'Message sent!'})

@app.route('/chat', methods=['GET'])
def get_chat():
    return jsonify(get_messages())  # Call function from chat.py

if __name__ == '__main__':
    app.run(debug=True)
