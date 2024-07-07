import re


def normalize_phone(phone_number: str) -> str:
    """
    :param phone_number: phone number in non-strict form
    :return: formatted phone number
    """
    phone_number = re.sub('[^0-9+]', '', phone_number)

    if phone_number[0] == '+':
        # Valid phone number
        return phone_number

    if len(phone_number) == 10:
        # For the phone numbers without country code
        return '+38' + phone_number

    if len(phone_number) == 12:
        # For the phone numbers with country code, but without + symbol
        return '+' + phone_number

    raise ValueError("Failed to parse phone number: " + phone_number)
