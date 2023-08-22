import inspect 

from Model import Model
from Validator import Parameter_Count_Validator as PCV
from Alg_Model_State import Alg_Model_State as State

class Algebraic_Model(Model):
    def __init__(self, representation):
        super().__init__(representation)

    def summary(self):
        func_source = inspect.getsource(self._representation)
        return f"I am an algebraic model using an equation:\n{func_source}"
    
    def sim_step(self, input):
        if self._validate_inputs(input) == False:
            raise ValueError(self.validation_log)
        
        output = self._representation(*input)
        self.__current_state = State(input, output)
        self._history.append(self.__current_state)

    def _validate_inputs(self, input):
        input_validator = PCV(input, self._representation)
        is_valid = input_validator.is_valid()        
        self.validation_log = input_validator.check_log()
        return is_valid
    
    def get_current_state(self):
        return self.__current_state
    
    def get_history(self):
        return self._history