class Errors:
    def positive_value_error(self, value):
        self.value = value
        if self.value < 0:
            raise Exception(f'Error this variable cannot take value like {self.value} use a positive value.')

    def lower_then_error(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value
        if first_value >= second_value:
            raise Exception(f'Error value {self.first_value} cannot be higher then {self.second_value}.')

    def duty_cycle_error(self, duty_cycle):
        self.duty_cycle = duty_cycle
        if self.duty_cycle <= 0 or self.duty_cycle >= 1:
            raise Exception(f'Error duty cycle cannot take value like {self.duty_cycle} use value from range(0,1).')

    def t_on_error(self, t_on, start_time, end_time):
        self.t_on = t_on
        self.start_time = start_time
        self.end_time = end_time
        if self.t_on < self.start_time or self.t_on > self.end_time:
            raise Exception(f'Error pulse time cannot take value like {self.t_on} use value from range(start_time, end_time).')