def triangle(a, b, c):
    return (a+b>c and a+b>c and b+c>a)


if __name__ == "__main__":
    print(triangle(3, 5, 4))
    print(triangle(-1, 2, 3))
    print(triangle(5, 9, 14))
    print(triangle(30, 12, 29))