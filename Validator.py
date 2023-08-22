import inspect

class Parameter_Count_Validator:
    def __init__(self, input, function):
        self.__input    = input
        self.__function = function

    def __analyse_input(self):
        parameters          = inspect.signature(self.__function).parameters
        inputs_count        = len(self.__input)
        inputs_required     = len(parameters)
        parameters_names    = list(parameters.keys())

        return inputs_count, inputs_required, parameters_names
    
    def is_valid(self):
        inputs_count, inputs_required, parameters_names = self.__analyse_input()
        return inputs_count == inputs_required

    def check_log(self):
        inputs_count, inputs_required, parameters_names = self.__analyse_input()
        if self.is_valid() == False:
            log = 'Invalid number of inputs.\n'
            log += f'Model required {inputs_required} parameters:\n'
            for parameter in parameters_names:
                log += f"  * {parameter}\n"
            log += f'\nGot {inputs_count} inputs instead'
        else:
            log = 'All gucci'

        return log