# killer4 en la rama 'rules'
class TurnManager:
    def __init__(self):
        self.turn = 0

    def next_turn(self):
        self.turn += 1
        print(f"Turn {self.turn}: Now it's {'White' if self.turn % 2 == 1 else 'Black'}'s turn")
