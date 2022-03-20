import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# convert a string to a float with one value, that has to be converted:
def convertSF1(term):
    converted = False
    while converted != True:
        edge_length_str = input("Pleaser enter " + term + " (in cm): " + Fore.LIGHTCYAN_EX)
        print(Fore.RESET)
        try:
            edge_length = float(edge_length_str)
            converted = True
            return edge_length
        except Exception:
            print(Fore.RED + "ValueError:" + Fore.YELLOW + " Input has to be an integer or float!" + Fore.RESET)
            continue
