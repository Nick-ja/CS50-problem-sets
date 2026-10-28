while True:
    fraction = input("Fraction: ")
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
        result = x / y * 100
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if x > y:
            pass
        elif round(result) >= 99:
            print("F")
            break
        elif round(result) <= 1:
            print("E")
            break
        else:
            print(f"{round(result)}%")
            break














