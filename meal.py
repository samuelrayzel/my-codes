def main():

    print('What time is it?')
    time = input()

    hours = convert(time)

    if(hours >= 7 and hours <=8):
        print('breakfest time')

    elif(hours >= 12 and hours <= 13):
        print('lunch time')\

    elif(hours >= 18 and hours <= 19):
        print('dinner time')

    else:
        print('')

def convert(t):

    t = t.strip()

    x, y = t.split(':')

    h = x.float()

    w = y.float()

    m = w/60

    d = h + m

    return d

main()
