from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

chat_log = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    username = data.get('username')

    if not message or not username:
        return jsonify({'error': 'Both username and message are required!'}), 400

    chat_log.append({'username': username, 'message': message})
    return jsonify({'success': True, 'message': 'Message sent!'})

@app.route('/chat', methods=['GET'])
def get_chat():
    return jsonify(chat_log[-10:])

if __name__ == '__main__':
    app.run(debug=True)
