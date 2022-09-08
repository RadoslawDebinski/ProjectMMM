import numpy as np
import errors as er

class Generator:
    def __init__(self, sample_rate):
        self.__warning = er.Errors()
        self.sample_rate = sample_rate

    def gen_sin(self, start_time, end_time, frequency, amplitude):
        self.start_time = start_time
        self.end_time = end_time
        self.frequency = frequency
        self.amplitude = amplitude

        self.__warning.positive_value_error(self.start_time)
        self.__warning.positive_value_error(self.end_time)
        self.__warning.lower_then_error(self.start_time, self.end_time)
        self.__warning.positive_value_error(self.sample_rate)
        self.__warning.positive_value_error(self.frequency)
        self.__warning.positive_value_error(self.amplitude)


        time = np.arange(self.start_time, self.end_time, 1 / self.sample_rate)
        sinewave = self.amplitude * np.sin(2 * np.pi * self.frequency * time)
        sinewave += self.amplitude
        return (time, sinewave)


    def gen_square_wave(self, start_time, end_time, period, duty_cycle, amplitude):
        self.start_time = start_time
        self.end_time = end_time
        self.period = period
        self.duty_cycle = duty_cycle
        self.amplitude = amplitude

        self.__warning.positive_value_error(self.start_time)
        self.__warning.positive_value_error(self.end_time)
        self.__warning.lower_then_error(self.start_time, self.end_time)
        self.__warning.positive_value_error(self.sample_rate)
        self.__warning.positive_value_error(self.period)
        self.__warning.duty_cycle_error(self.duty_cycle)
        self.__warning.positive_value_error(self.amplitude)

        time = np.arange(self.start_time, self.end_time, 1 / self.sample_rate)
        square_wave = []
        square_wave_sample = 0
        period_number = 1

        while square_wave_sample < len(time):
            if square_wave_sample <= self.period * self.duty_cycle + (period_number - 1) * self.period:
                square_wave.append(self.amplitude)
            else:
                square_wave.append(0)
            if square_wave_sample == self.period * period_number:
                period_number += 1
            square_wave_sample += 1

        return (time, square_wave)

    def gen_pulse(self, start_time, end_time, t_on, amplitude):
        self.start_time = start_time
        self.end_time = end_time
        self.t_on = t_on
        self.amplitude = amplitude

        self.__warning.positive_value_error(self.start_time)
        self.__warning.positive_value_error(self.end_time)
        self.__warning.lower_then_error(self.start_time, self.end_time)
        self.__warning.positive_value_error(self.sample_rate)
        self.__warning.t_on_error(self.t_on, self.start_time, self.end_time)
        self.__warning.positive_value_error(self.amplitude)

        time = np.arange(self.start_time, self.end_time, 1 / self.sample_rate)
        pulse = []
        pulse_sample = 0

        while pulse_sample < len(time):
            if pulse_sample < (self.t_on - self.start_time) * self.sample_rate:
                pulse.append(0)
            else:
                pulse.append(self.amplitude)
            pulse_sample += 1

        return (time, pulse)













