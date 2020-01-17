import random, os, sys

def estimated_random_normal_tens(random_number, com_guess) :
    rand_num  = random.randint(random_number, random_number)
    com_guess = com_guess

    # number below 10
    if len(str(rand_num)) == 1 :
        com_guess = random.randint(1, 10)

        return com_guess
    
    # number 10 and above
    else :
        get_num = str(rand_num)
        first_digit_num = str(get_num[0])
        fin_first_digit_num = int(first_digit_num)

        last_digit_num  = str(str(get_num[1:None]))
        fin_last_digit_num  = int(last_digit_num)

        if fin_last_digit_num > 5 or fin_last_digit_num == 5:
            fin_last_digit_num = 0
            if fin_last_digit_num == 0 :
                fin_first_digit_num += 1
        
        elif fin_last_digit_num < 5 :
            fin_last_digit_num = 0

        get_number = str(fin_first_digit_num) + str(fin_last_digit_num)
        get_number = int(get_number)
        guess_num  = random.randint(get_number-10, get_number)

        com_guess  = guess_num
        return com_guess
