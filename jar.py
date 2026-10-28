class Jar:
    def __init__(self, capacity=12):
        # __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
        self.amount = 0
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity

    def __str__(self):
        # __str__ should return a str with n 🍪, where n is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
        return self.amount * "🍪"

    def deposit(self, n):
        # deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
        if self.amount + n <= self._capacity:
            self.amount += n
            print(f"You deposited {n} cookies")
            return self.amountcd
        else:
            raise ValueError

    def withdraw(self, n):
        # withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
        if self.amount - n >= 0 and n < self._capacity:
            self.amount -= n
            print(f"You have withdraw {n} cookies")
            return self.amount
        else:
            raise ValueError

    @property
    def capacity(self):
        # capacity should return the cookie jar’s capacity.
        return self._capacity

    @property
    def size(self):
        # size should return the number of cookies actually in the cookie jar, initially 0.
        return self.amount

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity


def main():
    jar = Jar()
    while True:
        choice = int(input("What would you like to do?\n"
                           "1. Check capacity\n"
                           "2. Check size\n"
                           "3. Deposit cookies\n"
                           "4. Withdraw cookies\n"
                           "5. Show cookies\n"
                           "6. Exit\n"))

        if choice == 1:
            print(jar.capacity)
        if choice == 2:
            print(jar.size)
        if choice == 3:
            deposit = int(input("Choose the amount to deposit: "))
            jar.deposit(deposit)
        if choice == 4:
            withdraw = int(input("Choose the amount to withdraw: "))
            jar.withdraw(withdraw)
        if choice == 5:
            print(jar.__str__())
        if choice == 6:
            break


if __name__ == "__main__":
    main()
