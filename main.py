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
