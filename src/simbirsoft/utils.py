from datetime import datetime


def get_fibbonachi_number_by_index(index: int) -> int:
    """Return i-th fibbonachi number assuming the sequence start with 0, 1, ... and first element has index 1"""
    if index < 1:
        raise ValueError("Only positive integers allowed")

    numbers = [0, 1]

    while len(numbers) < index:
        next_value = numbers[-1] + numbers[-2]
        numbers.append(next_value)

    return numbers[index - 1]


def get_day_number() -> int:
    now = datetime.now()
    return now.day
