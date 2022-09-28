# Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of\n
# the integer's divisors(except for 1 and the number itself), from smallest to largest. \n
# If the number is prime return the string '(integer) is prime'
def divisors(integer):
    list_divisors = []
    for i in range(2, integer):
        work = integer
        if work % i == 0:
            list_divisors.append(i)
    if len(list_divisors) == 0:
        str = (f'{integer} is prime')
        return str
    else:
        return list_divisors

print(divisors(253))