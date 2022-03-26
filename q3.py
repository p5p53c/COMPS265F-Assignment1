from sys import stdin


def Divide_conquer(array):
    if len(array) == 1:
        return array[0]
    else:
        m1 = Divide_conquer(array[:len(array) // 2])
        m2 = Divide_conquer(array[len(array) // 2:])
        if m1 > m2:
            return m2
        else:
            return m1


def main():
    array = []
    for line in stdin:
        array.append(int(line))

    result = Divide_conquer(array)
    print(f"The minimum number is {result}")


if __name__ == "__main__":
    main()
