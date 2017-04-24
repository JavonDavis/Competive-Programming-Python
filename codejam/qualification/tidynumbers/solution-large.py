def number_of_digits(number):
    return len(str(number))


def threshold(number, power):
    if power == 0:
        return number
    else:
        return number * pow(10, power) + threshold(number, power-1)


def generate_last_tidy_number(x):
    num_digits = number_of_digits(x)
    p = int(str(x)[0])
    if num_digits == 1:
        return x
    elif x < threshold(p, num_digits-1):
        current_tens = (p-1) * pow(10, num_digits - 1)
        return current_tens + threshold(9, num_digits-2)
    else:
        current_tens = p * pow(10, num_digits - 1)
        return current_tens + generate_last_tidy_number(x - current_tens)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    print "Case #{}: {}".format(i, generate_last_tidy_number(n))

