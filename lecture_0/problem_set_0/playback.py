def playback(u_input):
    return u_input.replace(" ", "...")


def main():
    user_input = input()
    print(playback(user_input))


main()
