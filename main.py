
# killer1 en la rama 'controller'
class GameController:
    def __init__(self):
        self.board = None
        self.players = []

    def start_game(self):
        self.board = ChessBoard()
        self.players = [Player("White"), Player("Black")]
        print("Game started!")

# killer3 en la rama 'pieces'
class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

# killer2 en la rama 'board'
class ChessBoard:
    def __init__(self):
        self.grid = self.create_board()

    def create_board(self):
        return [["" for _ in range(8)] for _ in range(8)]

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def move(self, new_position):
        # Validate rook's movement
        super().move(new_position)
        
    def display_board(self):
        for row in self.grid:
            print(row)
