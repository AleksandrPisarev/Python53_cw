#1
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# d = int(input("Введите четвертое число: "))
# min = a
# if min > b:
#     min = b
# if min > c:
#     min = c
# if min > d:
#     min = d
# print(min)

#2

#3
# n = int(input('Введите сторону квадрата: '))
# for i in range(n):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(n-i):
#         print("*", end="")
#     print()

#4
# n = int(input('Введите число: '))
# sum = 0
# count = 0
# while n != 0:
#     sum+=n
#     count+=1
#     n = int(input('Введите число: '))
# print(sum/count)

#5
# import random
# begin = int(input('Начало: '))
# end = int(input('Конец: '))
# list1 = [0,0,0,0,0,0,0,0,0,0]
# for i in range(10):
#     list1[i] = random.randint(begin,end)
# print(list1)

#6
# list1 = [7,75,9,2,6,97,63,3,]
# size = len(list1)
# min = list1[0]
# index = 0
# for i in range(1,size):
#     if min > list1[i]:
#         min = list1[i]
#         index = i
# print(index)

#7
# list1 = [4,66,7,4,2,86,44,97,5,10]
# list2 = [0,0,0,0,0,0,0,0,0,0]
# def _copy(_list1, _list2):
#     size = len(_list1)
#     for i in range(size):
#         _list2[i] = _list1[i]
#     print(_list1)
# _copy(list1,list2)

#9
# import random
# n = int(input('Введите размер списка: '))
# def foo(n):
#     list1 = []
#     a = int(input('Начало диапазона: '))
#     b = int(input('Конец диапазона: '))
#     for i in range(n):
#         list1.append(random.randint(a,b))
#     print(list1)
# foo(n)

# n = int(input('Введите число: '))
# list1 = [4,66,7,4,2,86,44,97,5,4,10]
# print(list1)
# def _del(_list, n):
#     for i in _list[:]:
#         if n == i:
#             _list.remove(i)
#     print(_list)
# _del(list1,n)

#8
# n = int(input('Введите число: '))
# list1 = [4,66,7,4,2,86,44,97,5,4,10]
# def _add(_list, n):
#     list1 = []

list1 = [3,4,5,65,77,63,2,576,454,3]
print(list1)
def _del(_list, pos, n):
    for i in range(n):
        _list.pop(pos)
    print(_list)
_del(list1, 3, 4)



