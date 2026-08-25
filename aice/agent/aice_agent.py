from reasoning_loop import run_reasoning_loop
from memory.session_memory import SessionMemory

class AICEAgent:
    def __init__(self):
        self.session = SessionMemory()

    def chat(self, user_message):
        return run_reasoning_loop(user_message, self.session)

