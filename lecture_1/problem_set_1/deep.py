def main():
    user_input = (
        input(
            "What is the Answer to the Great Question of Life, the Universe, and Everything?: "
        )
        .lower()
        .strip()
    )

    print(deep(user_input))


def deep(s):
    if s == "42" or s == "forty-two" or s == "forty two":
        return "Yes"
    else:
        return "No"


main()
