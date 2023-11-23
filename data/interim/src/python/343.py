from abc import ABC, abstractmethod

class IGameRules(ABC):
    
    @abstractmethod
    def valid_move(self, move):
        pass
    
    @abstractmethod
    def game_over(self, board):
        pass
    
    @abstractmethod
    def check_win(self, board):
        pass
