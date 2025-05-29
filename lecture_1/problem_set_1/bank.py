def main():
    user_input = input("Greeting: ").lower().strip()

    if user_input.startswith("hello"):
        pay = "$0"
    elif user_input.startswith("h"):
        pay = "$20"
    else:
        pay = "$100"

    print(pay)


main()
