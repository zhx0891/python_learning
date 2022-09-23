#print ('hello python')
#a=input() #считывает данные с ввода
#i=int(input())
#f=float(input())
#c=None
#print (type(a)) #возвращает тип данных а
#str = 'строка'
#print(f'{a} _ {b} _ {str}') # интерполяция
#print('{} _ {} _ {}'.format(a,b,str))
#print('{2} _ {1} _ {0}'.format(a,f,str))
#T=True #логические переменные 
#F=False

#list =['1', '2', 1, 4.5,T] # возможность разнотипных списков
#print (list)
#i=+21 #унарный плюс
#print(i)
#i=-21 #унарный минус
#print (i)
#print(i/f) #деление по умолчанию как для вещественных чисел
#print(i//f) #деление в целых числах
#print(i%f)#остаток при делении
#print(i**i) #возведение в степень
#print(round(4.5 * 3, 2)) # 2 количество знаков после запятой
#i+=5
#i*=3
from tkinter import W
from traceback import format_tb


#log = 1 < 5
#print (log) #true 
#f=[2,5,1,5]
#print(2 in f) #true так как 2 содержится в  f
#exm_t =not f[0]%2 # не ноль поэтому true
#print(exm_t)
#a= int (input(' a = '))
#b= int (input(' b = '))
#if a > b:
#    print(a)
#else:
#    print(b)

org =45
inv = 0
while org !=0:
    inv =inv*10 + (org%10)
    org //=10
else:
    print(' достаточно')
print(inv)


for i in  1,33,5,6,4:
    print(i*2)

list = (33,5,6,4)
for i in list:
    print(i**i)     

r = range(10)
for i in r:
    print(i)

for i in range(5, 10, 2):
    print(i)

for i in 'qwerqwerqwerqwe':
    print(i)
