conversation = []

def add(role, message):
    conversation.append({
        "role": role,
        "content": message
    })

def get():
    return conversation