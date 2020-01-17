import random, os, sys

def estimate_and_set_random(min_value, max_value) :
    rand_num = random.randint(min_value, max_value)
    get_rand = str(rand_num)

    # Master
    if rand_num in range(500, 999) :
        if len(str(rand_num)) == 3 :
            first_digit  = get_rand[0]
            second_digit = get_rand[1]
            last_digit   = get_rand[2]
            estimated    = estimate_tens(second_digit, last_digit)

            if estimated == 100 :
                first_digit  = int(first_digit)
                first_digit += 1
                guess_num = str(first_digit) + str(str(estimated)[-2:])
                guess_num = int(guess_num)
                guess    = random.randint(guess_num - 10, guess_num)

                return guess
            
            else :
                guess_num = str(first_digit) + str(str(estimated)[-2:])
                guess_num = int(guess_num)
                guess   = random.randint(guess_num - 5, guess_num + 5)

                return guess
    
    # Hard
    elif rand_num in range(100, 499) :
        if len(str(rand_num)) == 3 :
            first_digit  = get_rand[0]
            second_digit = get_rand[1]
            last_digit   = get_rand[2]
            estimated    = estimate_tens(second_digit, last_digit)

            if estimated == 500 :
                first_digit  = int(first_digit)
                first_digit += 1
                guess_num = str(first_digit) + str(str(estimated)[-2:])
                guess_num = int(guess_num)
                guess    = random.randint(guess_num - 10, guess_num - 1)

                return guess
            
            else :
                get_num = str(first_digit) + str(str(estimated)[-2:])
                guess   = random.randint(int(get_num)-5, int(get_num)+5)

                return guess

    # Normal
    elif rand_num in range(11, 99) :
        if len(str(rand_num)) == 2 :
            first_digit  = get_rand[0]
            second_digit = get_rand[1]
            get_tens     = rand_num
            estimated    = estimate_tens(first_digit, second_digit)

            if estimated == 100 :
                guess = random.randint(estimated - 10, estimated - 1)
                return guess

            else :
                guess = random.randint(estimated - 5, estimated + 5)
                return guess

    # Easy
    elif rand_num in range(1, 10) :
        return random.randint(min_value, max_value)

def estimate_tens(first_digit_num, second_digit_num) :
    first_digit  = int(first_digit_num)
    second_digit = int(second_digit_num) 

    if second_digit > 5 or second_digit == 5:
        second_digit = 0
        if second_digit == 0 :
            first_digit += 1
    
    elif second_digit < 5 :
        second_digit = 0

    estimated = str(first_digit) + str(second_digit)
    return int(estimated)
