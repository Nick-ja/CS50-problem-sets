grocery_list = {}

while True:
    try:
        item = input().lower()
    except EOFError:
        break

    if item in grocery_list:
        grocery_list[item] += 1
    else:
        grocery_list[item] = 1

sorted_list = sorted(grocery_list.items())

for x, y in sorted_list:
    print(y, x.upper())


























