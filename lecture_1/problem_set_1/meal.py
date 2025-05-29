def main():
    user_input = input("What time is it? ")

    time_converted = convert(user_input.strip())

    if 7 <= time_converted <= 8:
        print("breakfast time")
    elif 12 <= time_converted <= 13:
        print("lunch time")
    elif 18 <= time_converted <= 19:
        print("dinner time")
    else:
        print("")


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + (float(minutes) / 60)


if __name__ == "__main__":
    main()
