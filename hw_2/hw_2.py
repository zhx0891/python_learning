# def sum_of_digit(n):
#  Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
def give_me_sequence(N):
    sequ =[]
    tmp = 1
    for i in range(1, N+1):
        tmp = tmp * i
        sequ.append(tmp)
    return sequ

print(give_me_sequence(4))
