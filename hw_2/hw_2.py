# def sum_of_digit(n):
#  Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
def second_task(N):
    sequ =[]
    tmp = 1
    for i in range(1, N+1):
        tmp = tmp * i
        sequ.append(tmp)
    return sequ


def third_task(n):
    ind = 0
    for i in range(1, n+1):
        ind += (1 + (1 / i)) ** i

    print(ind)
    return round(ind, 3)






# print(second_task(4))
print(third_task(6))