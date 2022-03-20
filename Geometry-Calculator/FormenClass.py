import math
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#------------------------------------------2D--------------------------------------------------------------------------------------

class Square():
    def __init__(self, edge_length):
        self.edge_length = edge_length

    def circumference(self):
        print("circumference: " + Fore.YELLOW + str(round(self.edge_length * 4, 2)) + "cm")

    def surface(self):
        print("surface: " + Fore.YELLOW + str(round(self.edge_length ** 2, 2)) + "cm²")

class Rectangle():
    def __init__(self, height, wide):
        self.height = height
        self.wide = wide

    def circumference(self):
        print("circumference: " + Fore.YELLOW + str(round((self.height + self.wide) * 2, 2)) + "cm")

    def surface(self):
        print("surface: " + Fore.YELLOW + str(round(self.height * self.wide, 2)) + "cm³")

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        print("circumference: " + Fore.YELLOW + str(round(2 * math.pi * self.radius, 2)) + "cm")

    def surface(self):
        print("surface: " + Fore.YELLOW + str(round(math.pi * self.radius**2, 2)) + "cm³")

#------------------------------------------3D--------------------------------------------------------------------------------------

class Cube():

    def __init__(self, edge_length):
        self.edge_length = edge_length

    def circumference(self):
        print("circumference: " + Fore.YELLOW + str(round(self.edge_length * 12, 2)) + "cm")

    def surface(self):
        print("per surface: " + Fore.YELLOW + str(round(self.edge_length ** 2, 2)) + "cm²")
        print("whole surface: " + Fore.YELLOW + str(round(self.edge_length ** 2 * 6, 2)) + "cm²")

    def volume(self):
        print("volume: " + Fore.YELLOW + str(round(self.edge_length ** 3, 2)) + "cm³\n")

class Quader():

    def __init__(self, height, wide, deep):
        self.height = height
        self.wide = wide
        self.deep = deep

    def circumference(self):
        print("circumference: " + Fore.YELLOW + str(round(4 * self.height + 4 * self.wide + 4 * self.deep, 2)) + "cm")

    def surface(self):
        surface_a = self.height * self.wide
        surface_b = self.height * self.deep
        surface_c = self.wide * self.deep

        print("surface_a: " + Fore.YELLOW + str(round(surface_a, 2)) + "cm²")
        print("surface_b: " + Fore.YELLOW + str(round(surface_b, 2)) + "cm²")
        print("surface_c: " + Fore.YELLOW + str(round(surface_c, 2)) + "cm²")
        print("whole surface: " + Fore.YELLOW + str(round(2 * surface_a + 2 * surface_b + 2 * surface_c, 2)) + "cm²")

    def volume(self):
        print("volume: " + Fore.YELLOW + str(round(self.height * self.wide * self.deep, 2)) + "cm³\n")

class Sphere():

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        print("circumference: " + Fore.YELLOW + str(round(2 * math.pi * self.radius, 2)) + "cm")

    def surface(self):
        print("surface: " + Fore.YELLOW + str(round(4 * math.pi * self.radius ** 2, 2)) + "cm²")

    def volume(self):
        print("volume: " + Fore.YELLOW + str(round(4/3 * math.pi * self.radius ** 3, 2)) + "cm³")

class Tetrahedron():

    def __init__(self, edge_length):
        self.edge_length = edge_length

    def surface(self):
        print("surface: " + Fore.YELLOW + str(round((self.edge_length**2)*math.sqrt(3), 2)) + "cm²")

    def volume(self):
        print("volume: " + Fore.YELLOW + str(round(self.edge_length ** 3 / 12 * math.sqrt(2), 2)) + "cm³\n")

class Octahedron():
    def __init__(self, edge_length):
        self.edge_length = edge_length

    def surface(self):
        print("surface: " + Fore.YELLOW + str(round((2*self.edge_length**2)*math.sqrt(3), 2)) + "cm²")

    def volume(self):
        print("volume: " + Fore.YELLOW + str(round((self.edge_length ** 3 * math.sqrt(2))/3, 2)) + "cm³\n")
