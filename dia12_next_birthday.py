from datetime import datetime, date


def calculator(date_birthday):
    now = date.today()
    next_date_birth = date(now.year, date_birthday.month, date_birthday.day)
    if next_date_birth < now:
        next_date_birth = date(
            now.year + 1, date_birthday.month, date_birthday.day)
    missing = next_date_birth - now
    missing = str(missing.days)
    return missing


def run():
    print("Welcome to Calculator the next birthday")
    birthday = input("Please, write your date of birth (dd/mm/yy)")
    formato = "%d/%m/%Y"
    date_birthday = datetime.strptime(birthday, formato)
    missing = calculator(date_birthday)
    print(missing+" days until your birthday!")


if __name__ == "__main__":
    run()
