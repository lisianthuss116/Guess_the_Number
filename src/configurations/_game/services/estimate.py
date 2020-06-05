import random
import time
import random


def estimate(mode, rnumber):
    minmax = {
        "easy": (1, 10, 5),
        "normal": (11, 99, 20),
        "hard": (100, 499, 10),
        "master": (500, 999, 5)
    }

    xmin, xmax, xnum = minmax.get(mode)

    def get_the_closest_value_of_random_number(rnumber, _min, _max, xnum):
        if rnumber - xnum < 1 or rnumber - xnum < _min:
            new_min = rnumber
        else:
            new_min = abs(rnumber - xnum)

        if rnumber + xnum > _max:
            new_max = rnumber
        else:
            new_max = rnumber + xnum

        new_number = random.randint(new_min, new_max)

        time.sleep(random.randint(1, 3))
        return new_number

    return get_the_closest_value_of_random_number(rnumber, xmin, xmax, xnum)
