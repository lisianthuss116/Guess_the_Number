import unittest
import random

import numpy


class EstimateRandomTest(unittest.TestCase):

    def get_the_closest_value_of_random_number(self, xmin, xmax):
        minim_number = 1
        maxim_number = 999
        number = random.randint(xmin, xmax)

        def template(number, _min, _max):
            new_min = number if number - 5 == 0 or number - 5 < number else abs(number - 5)
            new_max = number if number + 5 > _max else number + 5
            new_number = random.randint(new_min, new_max)

            assert_err = f"number must be between {_min} and {_max} | the number {new_number} | the actual-number {number}."
            assert(new_number >= _min and new_number <= _max), assert_err

        """master"""
        if number in range(500, 499):
            template(number=number, _min=500, _max=999)

        """hard"""
        if number in range(100, 499):
            template(number=number, _min=100, _max=499)

        """normal"""
        if number in range(20, 99):
            template(number=number, _min=20, _max=99)

        """easy"""
        if number in range(1, 19):
            template(number=number, _min=1, _max=19)

        if number < minim_number and number > maxim_number:
            assert(True), "number must be between {1} and {2}.".format(
                minim_number, maxim_number)

    def test_one_to_ten(self):
        # easy
        # check if the random number is between 1 and 19
        self.get_the_closest_value_of_random_number(1, 19)

    def test_eleven_to_nine2(self):
        # normal
        # check if the random number is between 20 and 99
        self.get_the_closest_value_of_random_number(20, 99)

    def test_onehundred_to_fourninenine(self):
        # hard
        # check if the random number is between 100 and 499
        self.get_the_closest_value_of_random_number(100, 499)

    def test_fivehundred_to_nine3(self):
        # master
        # check if the random number is between 500 and 999
        self.get_the_closest_value_of_random_number(500, 999)
