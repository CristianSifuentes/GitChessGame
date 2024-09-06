# killer3 en la rama 'pieces'
class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def move(self, new_position):
        self.position = new_position
        print(f"Piece moved to {new_position}")

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def move(self, new_position):
        # Validate rook's movement
        super().move(new_position)
# killer1 en la rama 'controller'
class GameController:
    def __init__(self):
        self.board = None
        self.players = []

    def start_game(self):
        self.board = ChessBoard()
        self.players = [Player("White"), Player("Black")]
        print("Game started!")
