expression = input("Expression: ")

x, y, z = expression.split(" ")

if y == "+":
    sum_x_y = float(x) + float(z)
    print(f"{sum_x_y:.1f}")

elif y == "-":
    subtr_x_y = float(x) - float(z)
    print(f"{subtr_x_y:.1f}")

elif y == "*":
    mult_x_y = float(x) * float(z)
    print(f"{mult_x_y:.1f}")

elif y == "/":
    div_x_y = float(x) / float(z)
    print(f"{div_x_y:.1f}")

