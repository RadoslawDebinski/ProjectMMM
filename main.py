from generator import Generator
from buckets import Bucket
import numpy as np
import matplotlib.pyplot as plt
import errors as er

generator = Generator(20)

vector1 = generator.gen_sin(0, 40, 1, 1)
vector2 = generator.gen_square_wave(40, 80, 20, 0.15, 2)
vector3 = generator.gen_pulse(80, 120, 85, 2)

vector_table = [vector1, vector2, vector3]

stream = [[], []]

for next_vector in vector_table:
    for moment, value in zip(next_vector[0], next_vector[1]):
        stream[0].append(moment)
        stream[1].append(value)


bucket1 = Bucket(stream[1], 2, 1)
outlet1 = bucket1.pour_water()
bucket2 = Bucket(outlet1[1], 0.1, 0.01)
outlet2 = bucket2.pour_water()

plik = open("testownik.csv", "w")
if plik.writable():
    for moment, input_value, height1, height2 in zip(stream[0], stream[1], outlet1[0], outlet2[0]):
        plik.write(f'{moment},{input_value},{height1},{height2}' + '\n')

plik.close()




