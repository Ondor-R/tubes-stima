from game.logic.base import BaseLogic

class MyBot(BaseLogic):
    def __init__(self, game_state):
        super().__init__(game_state)

    def next_move(self):
        # Implementasi greedy logic sederhana (contoh: gerak ke kanan terus)
        return (1, 0)
    