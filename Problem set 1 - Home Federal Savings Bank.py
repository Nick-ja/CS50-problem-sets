greeting = input("Greeting: ")

if "Hello" in greeting:
    print("$0")
elif greeting.startswith("H"):
    print("$20")
else:
    print("$100")
