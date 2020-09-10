from tree import Node

class KnightPathFinder:
    def __init__(self, coordinates):
        self._root = Node(coordinates)
        self._considered_positions = set([coordinates])

    def get_valid_moves(self, pos):
        (x, y) = pos
        valid_moves = {(x+1, y), (x+1, y-1), (x-1, y-1), (x-1, y), 
        (x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1)}
        return valid_moves

    def new_move_positions(self, pos):
        available_moves = self.get_valid_moves(pos) - (self._considered_positions)
        self._considered_positions = self._considered_positions | available_moves
        return available_moves

    


finder = KnightPathFinder((0, 0))
print(finder.new_move_positions((0, 0)))
