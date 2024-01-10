import os
import pickle
from datetime import datetime
import shutil


class User:

    def __init__(self, user: str):
        self.user = user
        self.path = f"histories/{user}.pickle"
        self.history = []
        self.last_login = datetime.now()
        self.agent_idx = 0
        if os.path.exists(self.path):
            with open(self.path, "rb") as f:
                previous_history: User = pickle.load(f)
            self.history = previous_history.history
            self.last_login = previous_history.last_login
            self.agent_idx = previous_history.agent_idx
            self.path = previous_history.path
            self.user = previous_history.user

    def add_user_message_to_history(self, message: str):
        self.history.append({"role": "user", "content": message})

    def add_assistant_message_history(self, message: str):
        self.history.append({"role": "assistant", "content": message})

    def save(self):
        # Super simple persistent storage
        self.last_login = datetime.now()
        if not os.path.exists("histories"):
            os.mkdir("histories")
        with open(self.path, "wb") as f:
            pickle.dump(self, f)
