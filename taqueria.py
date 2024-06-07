d = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

total = round(total, 2)

while True:

    pedido = input("Item: ")

    pedido = pedido.title()

    try:

        if pedido in d:

            total = total + d[pedido]

            print(f"Total: ${total}")

        elif pedido == "control-d":

            print(f"Total: ${total}")
            break

    except EOFError:

            break

    except KeyError:
            print(f"Total: ${total}")

            continue


