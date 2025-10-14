# a=int(input('Введите начало диапазона: '))
# b=int(input('Введите конец диапазона: '))
# if a > b:
#     a,d = b,a
# for i in range(b,a-1,-1):
#     print(i, end=" ")

# n=int(input('Введиете сколько чисел нужно ввести: '))
# count=0
# for i in range(1, n+1):
#     a=int(input(f'Введите {i} число: '))
#     if a%2 == 0: count+=1
# print(count)

marks=[3,41,465,3,63,3,89]
marks2=[1,2,3,41]
# sum=0
# max=marks[0]
# min=marks[0]
# for i in range (5, -1, -1):
#     print(marks[i], end=" ")
# print()
# for i in range(6):
#     sum+=marks[i]
# print(sum)
# for i in range(6):
#     if max < marks[i]:
#         max = marks[i]
#     if min >marks[i]:
#         min = marks[i]
# print(max, " ", min)

#1
# kol=0
# for i in marks:
#     count = 1
#     for j in range(i):
#         i=i//10
#         if i == 0:
#             break
#         else:
#             count+=1
#     if  count == 2:
#         kol+=1
# print(kol)

#3
# print(marks)
# for i in range(len(marks)//2):
#     marks[i],marks[len(marks)-1-i]=marks[len(marks)-1-i],marks[i]
# print(marks)

#4
# flag=0
# value=int(input('Введите число: '))
# for i in range(len(marks)):
#     if value == marks[i]:
#         print("Число есть в списке.")
#         flag=1
#         break
# if flag == 0:
#     print('Данного числа нет в списке.')

#5
# count=0
# for i in range(len(marks)):
#     for j in range(len(marks2)):
#         if marks[i] == marks2[j]:
#             count+=1
#             break
# print(count)

#6
# count=0
# size=len(marks)
# for i in range(size):
#     flag=0
#     for j in range(size):
#         if i == j: continue
#         if marks[i] == marks[j]:
#             flag=1
#             break
#     if flag == 0:
#         count+=1
# print(count)

#7
size1=len(marks)
size2=len(marks2)
print(marks)
print(marks2)
for i in range(size1):
    for j in range(size2):
        flag=0
        if marks[i] == marks2[j]:
            for k in range(i):
                if marks[k] == marks[i]:
                    flag=1
                    break
            if flag ==0:
                print(marks[i], end=" ")