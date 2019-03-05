from random import choice

class Player:
    def __init__(self, name):
        self.name = name
        self.bullets = 0
        self.guards = 5
        self.score = 0
        self.state = None
        """
        Possible States:
            - Reloading
            - Guarding
            - Shooting
        """

class RandomAI(Player):
    def __init__(self, name):
        super().__init__(name)

    def analyze(self):
        if self.bullets == 0 and self.guards == 0:
            return 1
        elif self.bullets == 0:
            return choice((1, 2))
        elif self.guards == 0:
            return choice((1, 3))
        else:
            return choice((1, 2, 3))
