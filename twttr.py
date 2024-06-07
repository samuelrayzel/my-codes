def remove_vowels(s):

    c = {"A","E","I","O","U","a","e","i","o","u"}

    for k in s:

        if((k in c) == True):

            s = s.replace(k, "")

    return s


def main():

    string = input("input: ")

    str = remove_vowels(string)

    print("output:", str)

main()
