def main():
    x, y, z = input("Expression: ").strip().split(" ")

    result = interpreter(x, y, z)

    print(f"{result:.1f}")


def interpreter(a, b, c):
    x = float(a)
    z = float(c)

    if b == "+":
        return x + z
    elif b == "-":
        return x - z
    elif b == "*":
        return x * z
    elif b == "/":
        return x / z


main()
