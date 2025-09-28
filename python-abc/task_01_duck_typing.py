#!/usr/bin/python3

from abc import ABC
import math


class Shape(ABC):
	def area(self):
		pass

	def perimeter(self):
		pass

class Circle(Shape):
	def __init__(self, area, perimeter):
		self.area = area
		self.perimeter = perimeter

class Rectangle(Shape):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height

	def perimeter(self):
		return 2 * (self.width +self.height)

def shape_info(Shape):
	print(f'Area: {shape.area()}')
	print(f'Perimeter: {shape.perimeter()}')

radius = float(input('Radius: '))
circle = Circle(radius=radius)
width = float(input('Width: '))
height = float(input('Height: '))
rectangle = Rectangle(width=width, height=height)
