# Программа получает число и возвращает список простых множителей.
print(' число?')
num = int(input())
for i in range(2, num):
    work=num
    if (work % i) == 0:
        print(f'{i}, ')
        work //= i
    else:
        if work != num:
            print(work)

