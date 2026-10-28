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

# prompting them for items, one per line
total = 0.00
while True:
    try:
        item = input("Item: ").title()  # Treat the user’s input case insensitively and every item on the menu will be title cased.
        price = float(d.get(item))
        total += price
    except EOFError:  # until the user inputs control-d
        print("\n")
        break
    except (TypeError, KeyError):  # Ignore any input that isn’t an item.
        pass
    else:
        print(f"${total:.2f}")  # After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places.









