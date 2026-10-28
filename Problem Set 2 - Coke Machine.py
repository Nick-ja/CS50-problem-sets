amount_due = 50
change_owed = 0

# Run loop as long as amount due is more than 0
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    insert_coin = int(input("Insert Coin: "))

    # Check if the coin entered is 25, 10 or 5
    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        amount_due -= insert_coin
    # If coin entered is not 25, 10 or 5
    else:
        amount_due = 50

    # If amount due is 0 or below, print change owed
    if amount_due <= 0:
        print(f"Change Owed: {change_owed - amount_due}")
    else:
        continue





