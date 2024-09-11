import random
from colorama import Fore, Style
from tabulate import tabulate


def main():
    print(f"{Fore.YELLOW}{'PASSWORD GENERATOR'.center(36, '=')}{Style.RESET_ALL}")
    password_length = get_password_length()
    password = generate_password(password_length)
    display_password(password)


def get_password_length():
    while True:
        try:
            password_length = int(input("Enter desired password length: "))
            if password_length < 14:
                print("ERROR: Strong password should be 14 characters or more")
            elif password_length > 50:
                print("ERROR: Keep password length <= 50 characters")
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
        random_number = generate_random_number(4)

        if random_number == 1:
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


def display_password(password):
    table = [[f"{Fore.GREEN}{"".join(password)}{Style.RESET_ALL}"]]
    print("\n" + tabulate(table, headers=[f"{Fore.RED}GENERATED PASSWORD{Style.RESET_ALL}"], tablefmt="github"))


if __name__ == "__main__":
    main()