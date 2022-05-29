from generator import Generator
from buckets import Bucket
import tkinter as tk


generator = Generator(20)
h = 0.1

vector1 = generator.gen_sin(0, 40, 1, 1)
vector2 = generator.gen_square_wave(40, 80, 20, 0.15, 2)
vector3 = generator.gen_pulse(80, 120, 85, 2)
generator = Generator(1/h)

vector_table = [vector1, vector2, vector3]
vector1 = generator.gen_sin(20, 40, 0.5, 1)
vector2 = generator.gen_square_wave(40, 60, 3/h, 0.7, 2)
vector3 = generator.gen_pulse(0, 20, 10, 2)

vector_table = [vector3, vector1, vector2]

stream = [[], []]

for next_vector in vector_table:
    for moment, value in zip(next_vector[0], next_vector[1]):
        stream[0].append(moment)
        stream[1].append(value)


bucket1 = Bucket(stream[1], 2, 1)
bucket1 = Bucket(stream[1], 2, 1, h)
outlet1 = bucket1.pour_water()
bucket2 = Bucket(outlet1[1], 0.1, 0.01)
bucket2 = Bucket(outlet1[1], 1, 0.1, h)
outlet2 = bucket2.pour_water()

print(f'{stream[0]}')

plik = open("testownik.csv", "w")
if plik.writable():
    for moment, input_value, height1, height2 in zip(stream[0], stream[1], outlet1[0], outlet2[0]):
        plik.write(f'{moment},{input_value},{height1},{height2}' + '\n')
plik.close()

print(f' {outlet1[0]} ')
my_w = tk.Tk()
widht, height = 810, 410
c_width, c_height = widht-10, height-10
d=str(widht) + "x" + str(height)
#btn1 = tk.Button(my_w, text='...')
#btn1.pack()
my_w.geometry(d)
c1=tk.Canvas(my_w, width=c_width, height=c_height, bg='lightblue')
c1.grid(row=0, column=0, padx=5, pady=5)
speed=5
x1,  y1 = 5,   int(c_height) - 5
h=y1-10
c1.create_line(x1,y1,c_width-5, y1, arrow='last')
c1.create_line(x1, y1, x1, 10, arrow='last')
c1.create_line(x1, y1, stream[0][500] * 10, outlet1[0][500] / 10000, fill='green', width=1)

def my_draw():
    i = 0
    if i<600:
        global x1, y1
        x2 = x1+ 50
        l1 = c1.create_line(x1, y1, x2, outlet1[0][i], fill='red', width=1)
        if (x1 < widht):
            x1, y1 = x2, outlet1[0][i]
            i=+1
            c1.after(speed, my_draw)
        else:
            return

my_draw()
my_w.mainloop()