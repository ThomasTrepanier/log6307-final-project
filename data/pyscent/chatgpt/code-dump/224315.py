from abc import ABC, abstractmethod

class MoveStrategy(ABC):
    @abstractmethod
    def select_move(self, game_state):
        pass

class HumanMoveStrategy(MoveStrategy):
    def select_move(self, game_state):
        position = int(input("Enter your move: "))
        return position

class ComputerMoveStrategy(MoveStrategy):
    def select_move(self, game_state):
        # Implement your move choosing algorithm here
        pass

class Player(ABC):
    def __init__(self, letter, move_strategy):
        self.letter = letter
        self.move_strategy = move_strategy

    def move(self, game_state):
        return self.move_strategy.select_move(game_state)
