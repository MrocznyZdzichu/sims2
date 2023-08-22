from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, input, output):
        self._u = input
        self._y = output

    def get_control(self):
        return self._u
    
    def get_output(self):
        return self._y