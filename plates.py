def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def shifts(string):

    x = 0

    w1 = False
    w2 = False

    for c in string:

        w1 = w2

        w2 = c.isnumeric()

        if(w1 != w2):

            x = x + 1

    return x



def first_number(f):

    answer = 1

    for c in f:

        w  = c.isnumeric()

        if(w == True):

            C = int(c)

            answer = C

            break

    return answer




def is_valid(s):

    X = s[0:2]

    ch = X.isnumeric()

    sh = shifts(s)

    l = len(s)

    a = first_number(s)

    if(ch == True):
        return False

    elif(l < 2 or l > 6):
        return False

    elif(a == 0 or sh > 1):
        return False

    elif(("." in s) == True):
        return False

    elif((" " in s) == True):
        return False

    elif(("?" in s) == True):
        return False

    elif(("!" in s) == True):
        return False

    elif((":" in s) == True):
        return False

    elif((";" in s) == True):
        return False

    elif(("," in s) == True):
        return False

    else:
        return True



main()
