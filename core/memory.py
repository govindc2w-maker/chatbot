class Memory:
    """Simple in-memory conversation history."""
    def __init__(self):
        self.history = []

    def add(self, role, message):
        self.history.append({"role": role, "parts": [message]})

    def get(self):
        return self.history
