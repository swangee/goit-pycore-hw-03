import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    :param min: must be 1 or more
    :param max: must be bigger than min and less or equal to 1000
    :param quantity: number of tickets, must be between min and max
    :return: list of numbers or empty list on invalid input
    """

    if min < 1:
        return []

    if max > 1000 or max <= min:
        return []

    if quantity < min or quantity > max:
        return []

    return random.sample(range(min, max), quantity)


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)