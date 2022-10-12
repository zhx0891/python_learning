# Напишите программу, которая принимает на вход число и показывает сумму его цифр.
# print('?')
# num = int(input())
# sum = 0
# while (num > 0):
#     sum = sum + num % 10
#     num //= 10
# print(sum)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# print('?')
# num = int(input())
# tmp = 1
# list_m = []
# ind = 0
# for i in range(1, num+1):
#     tmp *= i
#     list_m.append(0)
#     list_m[ind] = tmp
#     ind += 1
# print(list_m)
# str_ = 'asdfasd asdfas dsafasd dfdfd sada '
# print(str_.split('a'))
# print(dir(str_))

# print('?')
# n = int(input())
# ind_ = 1
# for i in range(1, n+1):
#     print(ind_)
#     ind_ *= -3
#
# def show_sequence(n):
#     for i in range(n):
#         num = (-3) ** i
#         print(num, end=' ')
#
#
# show_sequence(5)

# программа находит количество заданных последовательностей в строке

# def count_sequence(list_, sequence):
#
#     count = 0
#     ind = 0
#     for i in list_:
#         if list_[ind] == sequence[0]:
#             j = 1
#
#             while j != len(sequence):
#                 if ind <= (len(list_) - len(sequence)):
#                     if list_[ind + j] == sequence[j]:
#
#                         j += 1
#                         if j == len(sequence):
#                             count += 1
#                             break
#                     else:
#                         break
#                 else:
#                     break
#         ind += 1
#
#     print(count)
#
# def count_sequence_two(str1, str2):
#     print(len(str1.split(str2))-1)
#
#
# count_sequence_two("weretriyrityrerere", "ere")


lst = [i for i in range(1, 21)]
print(lst)