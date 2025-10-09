# sum=0
# count=0
# while True:
#     try:
#         value = int(input('Введите число кратное 5: '))
#     except ValueError:
# #         print('Ведено не числовое значение. Введите число.\n')
#     else:
#         if value%5 == 0:
#             break
#         else:
#             sum+=value
#             count+=1
# print(sum/count)

# while True:
#     count=2
#     flag=0
#     try:
#         value=int(input('Введите число: '))
#     except ValueError:
#          print('Ведено не числовое значение. Введите число.\n')
#     else:
#         while count<value:
#            if value%count == 0:
#                 flag=1
#                 break
#            else :
#                count+=1
#         if flag ==1:
#             print('Введено не простое число')
#         else:В
#             print('Введено простое число')
#         break

# _min=int(input('Введите начало диапазона: '))
# _max=int(input('Введите конец диапазона: '))
# if _min>_max: _min,_max=_max,_min
# if _max%2: _max-=1
# for i in range(_max,_min-1,-2):
#     print(i, end=" ")

# value=int(input('Введите сторону квадрата: '))
# for i in range(value):
#     for j in range(value-i):
#         print('*', end=" ")
#     print("\n")

# value=int(input('Введите сторону квадрата: '))
# for i in range(value):
#     for j in range(i):
#         print(' ', end=" ")
#     for j in range(value-i):
#         print('*', end=" ")
#     print("\n")

# value=int(input('Введите сторону квадрата: '))
# for i in range(value):
#     for j in range(value-(i+1)):
#         print(' ', end=" ")
#     for j in range(i+1):
#         print('*', end=" ")
#     print("\n")

# value=int(input('Введите сторону квадрата: '))
# for i in range(value):
#     for j in range(i):
#         print(' ', end=" ")
#     for j in range(value):
#         print('*', end=" ")
#     for j in range(i):
#         print(' ', end=" ")
#     value-=2
#     print("\n")

value=int(input('Введите сторону квадрата: '))
for i in range(value):
    for j in range((value-1)/2):
        print(' ', end=" ")
    for j in range(i+1):
        print('*', end=" ")
    for j in range((value-1)/2):
        print(' ', end=" ")
    print("\n")