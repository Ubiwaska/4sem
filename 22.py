#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n – кол – во элементов первого  множества. m – кол – во элементов второго множества.
#Затем пользователь вводит сами элементы множеств. (Попробуйте использовать множества и их пересечение).

n = (int(input('Введите количество элементов первого множества: ')))
m = (int(input('Введите количество элементов второго множества: ')))
list_n = [] 
list_m = []
print('Введите целые числа первого множества:')
for i in range(n):
    list_n.append(int(input()))
    i += i
print('Введите целые числа второго множества:')
for i in range(m):
    list_m.append(int(input()))
    i += i
print(list_n)
print(list_m)
print(sorted(set(list_n).intersection(set(list_m))))