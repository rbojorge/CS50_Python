def calculate_e(mass):
    return mass * pow(300000000, 2)


def main():
    m = int(input("m:"))
    print(f"E: {calculate_e(m)}")


main()
