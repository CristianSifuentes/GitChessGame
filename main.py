# killer1 en la rama 'controller'
class GameController:
    def __init__(self):
        self.board = None
        self.players = []

    def start_game(self):
        self.board = ChessBoard()
        self.players = [Player("White"), Player("Black")]
        print("Game started!")
