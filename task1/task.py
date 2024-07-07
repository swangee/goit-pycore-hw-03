from datetime import datetime


def get_days_from_today(date: str) -> int | None:
    """
    :param date: Pass date in the yyyy-mm-dd format
    :return: int on success, None on failure
    """

    today = datetime.today()

    try:
        date_obj = datetime.strptime(
            date,
            '%Y-%m-%d'
        )
    except ValueError as e:
        print("invalid date passed, please use yyyy-mm-dd format")
        return

    diff = today - date_obj

    return diff.days
