# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# print('?')
# num = int(input())
# sum = 0
# while (num > 0):
#     sum = sum + num % 10
#     num //= 10
# print(sum)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

print('?')
num = int(input())
tmp = 1
list_m = []
ind = 0
for i in range(1, num+1):
    tmp *= i
    list_m.append(0)
    list_m[ind] = tmp
    ind += 1
print(list_m)