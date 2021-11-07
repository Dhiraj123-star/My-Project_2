def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")

# calling the normal function

#ordinary()

#calling generator function

pretty = make_pretty(ordinary)

pretty()