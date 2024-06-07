import random

while True:

    x = input("Level: ")

    try:

        i = int(x)

        r = random.randint(1,i)

        while True:

            g = input("Guess: ")

            G = int(g)

            if(G > r):

                print("Too large!")

                continue

            elif(G < r):

                print("Too small!")

                continue

            else:

                print("Just right!")

                break

        break

    except ValueError:
        continue
