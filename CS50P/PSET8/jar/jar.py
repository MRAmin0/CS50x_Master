class Jar:
    def __init__(self, capacity=12, size =0):
        # initialize a cookie jar with the given capacoty
        self.capacity = capacity
        self.size = size

    def __str__(self):
        # return a str with 🍪, where is the number of cookies
        return "🍪" * self.size
    def deposit(self, n):
        # add n cookies to the cookie jar.
        if not n > (self.capacity -self.size):
            self.size += n
        else:
            raise ValueError("Too many cookies!")

    def withdraw(self, n):
        # should remove n cookies from the cookie jar
        if not n > self.size:
            self.size -= n
        else:
            raise ValueError("Too few cookies!")

    # getter
    @property
    def capacity(self):
        # return the cookie jar's capacity
        return self._capacity

    @property
    def size(self):
        #return the number of cookies actually in the cookie jar
        return self._size

    # setter
    @capacity.setter
    def capacity(self , capacity):
        if not int(capacity) > 0:
            raise ValueError("Not a non-negative integer.")
        self._capacity = capacity

    @size.setter
    def size(self , size):
        if int(siez) < 0"
            raise ValueError
        else:
            self._size = size

def main():
    # Run the main code
    if __name__ = "__name__":
        main()


