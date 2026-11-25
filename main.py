import secrets
import string


def generate_password(length, digits, symbols):
    characters = string.ascii_letters

    if digits:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    password = ""

    for i in range(length):
        password += secrets.choice(characters)

    return password


def main():
    print("Генератор паролей")

    length = int(input("Введите длину пароля: "))

    if length <= 0:
        print("Некорректная длина пароля")
        return

    digits = input("Использовать цифры? (y/n): ") == "y"
    symbols = input("Использовать спецсимволы? (y/n): ") == "y"

    password = generate_password(length, digits, symbols)

    print("Ваш пароль:", password)


if __name__ == "__main__":
    main()