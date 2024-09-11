import random


def main():
    password_length = get_password_length()
    password = generate_password(password_length)
    print("".join(password))


def get_password_length():
    while True:
        try:
            password_length = int(input("Enter desired password length: "))
            if password_length < 14:
                print("ERROR: Strong password should be 14 characters or more")
            else:
                return password_length

        except ValueError:
            print("ValueError: Please enter a number")


def generate_random_number(x):
    return random.randint(1, x)


def generate_password(password_length):
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_characters = r"!@#$%^&*()_-=+{}[]:;',.<>?/\|~`"

    password = []
    counter = 0

    while counter < password_length:
        # chooses which category to grab from
        random_number = generate_random_number(4)

        if random_number == 1:
            # get a letter from letters list and append to password
            index = generate_random_number(len(lowercase_letters) - 1)
            password.append(lowercase_letters[index])

        elif random_number == 2:
            index = generate_random_number(len(uppercase_letters) - 1)
            password.append(uppercase_letters[index])

        elif random_number == 3:
            index = generate_random_number(len(numbers) - 1)
            password.append(numbers[index])

        else:
            index = generate_random_number(len(special_characters) - 1)
            password.append(special_characters[index])

        counter += 1

    return password


if __name__ == "__main__":
    main()
