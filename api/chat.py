chat_log = []

def add_message(username, message):
    """Add a message to the chat log."""
    chat_log.append({'username': username, 'message': message})

def get_messages():
    """Retrieve the last 10 messages."""
    return chat_log[-10:]
