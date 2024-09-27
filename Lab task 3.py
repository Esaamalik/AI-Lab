class ModelBasedReflexAgent:
    def __init__(self):
        self.location = (0, 0)
        self.environment = {}

    def perceive(self, state):
        self.environment[self.location] = state

    def act(self):
        if self.location in self.environment:
            if self.environment[self.location] == 'dirty':
                print(f"Cleaning at {self.location}")
                self.environment[self.location] = 'clean'
                return 'clean'
            else:
                print(f"Moving from {self.location}")
                self.move()
        else:
            print(f"Unknown location: {self.location}")

    def move(self):
        self.location = (self.location[0], self.location[1] + 1)

agent = ModelBasedReflexAgent()
agent.perceive('dirty')
agent.act()
agent.act()
agent.perceive('clean')
agent.act()