from generator import Generator
import numpy as np
import matplotlib.pyplot as plt
import errors as er

generator = Generator()

vector1 = generator.gen_sin(0, 10, 20, 1, 2)
vector2 = generator.gen_square_wave(10, 20, 20, 10, 0.5, 2)
vector3 = generator.gen_pulse(20, 30, 20, 27, 2)

for moment, value in zip(vector1[0], vector1[1]):
  print(f'{moment} {value}' + '\n')

for moment, value in zip(vector2[0], vector2[1]):
  print(f'{moment} {value}' + '\n')

for moment, value in zip(vector3[0], vector3[1]):
  print(f'{moment} {value}' + '\n')