import random

def main():

    while True:

        nivel = get_level()

        try:

            score = 0
            i = 0

            while i < 10:
                Z = generate_integer(nivel)

                mistakes = 0

                x1 = str(Z[0])
                y1 = str(Z[1])

                while mistakes < 3:


                    answer = input(f"{x1} + {y1} = ")

                    try:

                        R = int(answer)

                        if R == Z[0] + Z[1]:

                            score = score + 1
                            i = i + 1
                            mistakes = 3

                        elif (R != Z[0] + Z[1]) and (mistakes == 2):

                            A = Z[0] + Z[1]
                            i = i + 1
                            print(f"{x1} + {y1} = {A}")
                            mistakes = mistakes + 1

                        else:
                            mistakes = mistakes + 1

                            print("EEE")

                            continue

                    except ValueError:
                            mistakes = mistakes + 1

                            print("EEE")

                            continue


        except ValueError:

            continue

def get_level():

        while True:

            level = input("Level: ")


            if level.isnumeric() == True:
                z = int(level)

                break

            else:

                continue



        return z



def generate_integer(level):



    if level == 1:
        X = random.randint(0,9)
        Y = random.randint(0,9)

        S = [X,Y]

        return S

    elif level == 2:

        X = random.randint(10,99)
        Y = random.randint(10,99)

        S = [X,Y]

        return S

    elif level == 3:

        X = random.randint(100,999)
        Y = random.randint(100,999)

        S = [X,Y]

        return S

    else:
        raise ValueError



main()
