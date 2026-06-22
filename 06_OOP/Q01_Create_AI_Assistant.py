class ChatAgent:

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def respond(self):
        print(f"{self.name} is responding as {self.role}")

agent = ChatAgent("PriyaGPT", "Python Tutor")

agent.respond()
