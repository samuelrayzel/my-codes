import random
import sys
from pyfiglet import Figlet

x = input("Input: ")

j = len(sys.argv) - 1

figlet = Figlet()

list = figlet.getFonts()


#no arguments after the file = random font

try:

    if j == 0:

        f = random.choice(list)
        figlet.setFont(font=f)
        print(figlet.renderText(x))

    #one argument after the file = sys exit and error

    elif j == 1:

        sys.exit()

    #two arguments after the file, but one of them is invalid = sys exit and error
    #else, we print according to the font chosen

    elif j == 2:

        if sys.argv[1] != "-f" and sys.argv[1] != "--font":

            sys.exit()

        elif (sys.argv[2] in list) == False:

            sys.exit()

        else:

            f = sys.argv[2]
            figlet.setFont(font=f)
            print(figlet.renderText(x))

except SystemExit as e:
    print("Invalid usage")
