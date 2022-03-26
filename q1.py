from sys import stdin


def subtractionsgcd(a, b):
    if a == b:
        return a
    elif a > b:
        print(f"({a - b}, {b})")
        return subtractionsgcd(a - b, b)
    else:
        print(f"({a}, {b - a})")
        return subtractionsgcd(a, b - a)


def modulogcd(a, b):
    try:
        if a > b:
            print(f"({a % b}, {b})")
            return modulogcd(a % b, b)
        else:
            print(f"({a}, {b % a})")
            return modulogcd(a, b % a)
    except ZeroDivisionError:
        if b == 0:
            return a
        else:
            return b


def main():
    a = int(stdin.readline())
    b = int(stdin.readline())
    print(f"Mutual subtractions: The GCD of {a} and {b} is {subtractionsgcd(a, b)}.")
    print(f"Modulo operations: The GCD of {a} and {b} is {modulogcd(a, b)}.")


if __name__ == "__main__":
    main()
