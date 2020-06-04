import random


def estimate(mode):
    minmax = {
        "easy": (1, 10),
        "normal": (11, 99),
        "hard": (100, 499),
        "master": (500, 999)
    }

    xmin, xmax = minmax.get(mode)

    number = random.randint(xmin, xmax)

    def get_the_closest_value_of_random_number(number, _min, _max):
        new_min = number if number - 5 < 1 or number - 5 < _min else abs(number - 5)
        new_max = number if number + 5 > _max else number + 5

        new_number = random.randint(new_min, new_max)

        return new_number

    return get_the_closest_value_of_random_number(number, xmin, xmax)
