def funcionou(s):

    try:

        x, y = s.split("/")

        X = int(x)
        Y = int(y)

        Z = (X/Y)

        w = round(Z,2)

        W = w*100



        if(W <= 1):
            return("E")

        elif(W >= 99 and W <=100):
            return("F")

        elif(W > 100):
            return False

        else:

            return(W)

    except ValueError:
        return True

    except ZeroDivisionError:
        return True


while True:

    fracao = input("Fraction: ")

    h = funcionou(fracao)

    if(h == "E"):
        print("E")

        break

    elif(h == "F"):
        print("F")

        break

    elif(h == True):
        continue

    elif(h == False):

        continue

    else:

        s = str(h)

        S = s.replace(".0", "")

        print(f"{S}%")

        break
