from abc import ABC, abstractmethod

class Model(ABC):
    def __init__(self, representation):
        self._representation    = representation
        self._history           = []
    
    @abstractmethod
    def summary(self):
        pass

    @abstractmethod
    def sim_step(self, input):
        pass

    @abstractmethod
    def _validate_inputs(self, input):
        pass