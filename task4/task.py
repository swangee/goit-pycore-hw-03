from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> list:
    """
    This function has a bug. If we moved congratulation_date to monday from the weekend
    than we won't see that user in the list on monday. To fix that - we also have to check
    if today is monday and users' bday was yesterday or 2 days ago.
    """
    result = []

    today = datetime.today().date()

    for user in users:
        upcoming_birthday = calc_upcoming_birthday_date(today, user["birthday"])
        if upcoming_birthday > (today + timedelta(days=7)):
            # Skip users with birthday date later than in a week
            continue

        result.append({"name": user["name"], "congratulation_date": calc_congratulation_date(upcoming_birthday)})

    return result


def calc_congratulation_date(upcoming_birthday: datetime.date) -> str:
    congratulation_date = upcoming_birthday
    if congratulation_date.isoweekday() > 5:
        # Move congrats date to the 1st iso weekday (monday) if weekday is saturday or sunday
        congratulation_date = congratulation_date + timedelta(8 - congratulation_date.isoweekday())

    return congratulation_date.strftime('%Y.%m.%d')


def calc_upcoming_birthday_date(today: datetime.date, birthday: str) -> datetime.date:
    birthday_date = datetime.strptime(birthday, "%Y.%m.%d").date()

    birthday_this_years = birthday_date.replace(year=today.year)
    congrats_date = birthday_this_years

    if birthday_this_years < today:
        congrats_date = congrats_date.replace(year=today.year+1)

    return congrats_date
