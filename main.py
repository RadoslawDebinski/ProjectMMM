from generator import Generator
from buckets import Bucket
import numpy as np
import matplotlib.pyplot as plt
import errors as er

h = 0.01

generator = Generator(1/h)

vector1 = generator.gen_sin(20, 40, 0.5, 1)
vector2 = generator.gen_square_wave(40, 60, 3/h, 0.7, 2)
vector3 = generator.gen_pulse(0, 20, 10, 2)

vector_table = [vector1, vector2, vector3]

stream = [[], []]

for next_vector in vector_table:
    for moment, value in zip(next_vector[0], next_vector[1]):
        stream[0].append(moment)
        stream[1].append(value)

bucket1 = Bucket(stream[1], 2, 0.3, h)
outlet1 = bucket1.pour_water()
bucket2 = Bucket(outlet1[1], 1, 0.5, h)
outlet2 = bucket2.pour_water()

plik = open("testownik.csv", "w")
if plik.writable():
    for moment, input_value, height1, height2 in zip(stream[0], stream[1], outlet1[0], outlet2[0]):
        plik.write(f'{moment},{input_value},{height1},{height2}' + '\n')

plik.close()




