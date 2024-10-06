"""
Jacob Smalley
6 Oct 2024
P2LAB1
Cirlce information calulator.
"""
import math

radius = float(input('What is the radius of the circle? '))
diameter = radius * 2
circumference = 2 * math.pi * radius
area = math.pi * radius**2

print(f'The diameter of the circle is: {diameter}')
print(f'The circumference of the circle is: {circumference:.2f}')
print(f'The area of the circle is: {area:.3f}')

while True:
    pass
