def convert(u_input):
    return u_input.replace(":)", "🙂").replace(":(", "🙁")


def main():
    user_input = input()
    print(convert(user_input))


main()
