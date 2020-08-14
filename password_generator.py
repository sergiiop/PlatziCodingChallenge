import string
import random


def generator_password(lon, mayus, minus, number, simbols):
    characteres = []
    password = []
    if mayus == 'y':
        characteres = characteres + list(string.ascii_uppercase)
    if minus == 'y':
        characteres = characteres + list(string.ascii_lowercase)
    if number == 'y':
        characteres = characteres + list(string.digits)
    if simbols == 'y':
        characteres = characteres + list(string.punctuation)
    for i in range(lon):
        character_random = random.choice(characteres)
        password.append(character_random)

    password = ''.join(password)
    return password


def run():
    menu = """
    Welcome to Password Generator
    To next your need tipe, how you like the password
    """
    print(menu)
    lon = int(input("Tipe the large of the password: "))
    mayus = input("¿Do you want the password has a Mayus? (y/n): ")
    minus = input("¿Do you want the password has a Minus? (y/n): ")
    number = input("¿Do you want the password has a number? (y/n): ")
    simbols = input("¿Do you want the password has a simbols? (y/n): ")
    password = generator_password(lon, mayus, minus, number, simbols)
    print('Your new password is: ' + password)


if __name__ == "__main__":
    run()
