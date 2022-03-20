import FormenClass as FC
import ShapesInputConversion as SIC
import math
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def twoD():
    print("Choose a geometric shape: ")
    print("Enter following options: ")
    print(Fore.YELLOW + "[S]" + Fore.WHITE + " => Square")
    print(Fore.YELLOW + "[R]" + Fore.WHITE + " => Rectangle")
    print(Fore.YELLOW + "[C]" + Fore.WHITE + " => Circle")
    print(Fore.YELLOW + "[D]" + Fore.WHITE + " => Change demension")

    choice = input("Please enter which geometric shape you want to convert: " + Fore.LIGHTCYAN_EX)
    print(Fore.RESET)

    if choice.lower() == "s":
        edge_length = SIC.convertSF1("edge-length")
        s = FC.Square(edge_length)
        s.circumference()
        s.surface()
        twoD()

    elif choice.lower() == "r":
        edge_length_a = SIC.convertSF1("edge-length-a")
        edge_length_b = SIC.convertSF1("edge_length_b")
        r = FC.Rectangle(edge_length_a, edge_length_b)
        r.circumference()
        r.surface()
        twoD()

    elif choice.lower() == "c":
        radius = SIC.convertSF1("radius")
        c = FC.Circle(radius)
        c.circumference()
        c.surface()
        twoD()

    elif choice.lower() == "d":
        print(home())

    elif choice.lower() == "x":
        exit()

def threeD():
    print("Choose a geometric shape: ")
    print("Enter following options: ")
    print(Fore.YELLOW + "[C]" + Fore.WHITE + " => Cube")
    print(Fore.YELLOW + "[Q]" + Fore.WHITE + " => Quader")
    print(Fore.YELLOW + "[S]" + Fore.WHITE + " => Sphere")
    print(Fore.YELLOW + "[T]" + Fore.WHITE + " => Tetrahedron")
    print(Fore.YELLOW + "[O]" + Fore.WHITE + " => Octahedron")
    print(Fore.YELLOW + "[D]" + Fore.WHITE + " => Change demension")
    print(Fore.YELLOW + "[X]" + Fore.WHITE + " => exit")

    choice = input("Please enter which geometric shape you want to convert: " + Fore.LIGHTCYAN_EX)
    print(Fore.RESET)

    if choice.lower() == "c":
        edge_length = SIC.convertSF1("edge-length")
        c = FC.Cube(edge_length)
        c.circumference()
        c.surface()
        c.volume()
        threeD()

    elif choice.lower() == "q":
        height = SIC.convertSF1("height")
        wide = SIC.convertSF1("wide")
        deep = SIC.convertSF1("deep")

        q = FC.Quader(height, wide, deep)
        q.circumference()
        q.surface()
        q.volume()
        threeD()

    elif choice.lower() == "s":
        radius = SIC.convertSF1("radius")
        s = FC.Sphere(radius)
        s.circumference()
        s.surface()
        s.volume()
        threeD()

    elif choice.lower() == "t":
        edge_length = SIC.convertSF1("edge-length")
        t = FC.Tetrahedron(edge_length)
        t.surface()
        t.volume()
        threeD()

    elif choice.lower() == "o":
        edge_length = SIC.convertSF1("edge-length")
        o = FC.Octahedron(edge_length)
        o.surface()
        o.volume()
        threeD()

    elif choice.lower() == "d":
        home()

    elif choice.lower() == "x":
        exit()

def home():
    print("Choose Demension of Shape: ")
    print("Enter following options: ")
    print(Fore.YELLOW + "[2D]" + Fore.WHITE + " => 2-Demensional")
    print(Fore.YELLOW + "[3D]" + Fore.WHITE + " => 3-Demensional")
    print(Fore.YELLOW + "[H]" + Fore.WHITE + " => Help")
    print(Fore.YELLOW + "[X]" + Fore.WHITE + " => exit")

    option = input("Please enter demension: " + Fore.LIGHTCYAN_EX)
    print(Fore.RESET)

    if option.lower() == "2d":
        twoD()

    elif option.lower() == "3d":
        threeD()

    elif option.lower() == "h":
        pass

    elif option.lower() == "x":
        exit()

print(home())
