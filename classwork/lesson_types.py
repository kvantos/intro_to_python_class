import numpy as np
import math

#  calculus of rectangle square
h = 10
w = 20
s = h * w
print("площадь прямоугольника с высотой %i и шириной %i будет: %i" % (h,w,s))

# calculate circle square
radius = 5
circle_square = np.pi * radius**2
print("Площадь круга с радиусом %d будет: %.2f" % (radius, np.round(circle_square, 2)))

# calculate hypotenuse
catheter_a = 5
catheter_b = 6
hypotenuse = np.sqrt(catheter_a**2 + catheter_b**2)
print("при катетах А = %d и В = %d, гипотенуза: %.2f" % (catheter_a, catheter_b, np.round(hypotenuse,2)))

