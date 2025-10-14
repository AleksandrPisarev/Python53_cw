list1 =  [2,3,4,3,5,6,7,3,8]
# for i in list1:
#     print(i, end=" ")
# print()
# for i in range(len(list1)):
#     print(list1[i], end=" ")
# print()
# it = iter(list1)
# for i in it:
#     print(i, end=" ")

# for i in range(len(list1)):
#     if list1[i]%2 != 0:
#         list1[i] = 0
# print(list1)

# size = len(list1)
# for i in range(size):
#     for j in range(i,size):
#         flag = 0
#         if i == j:
#             continue
#         if list1[i] == list1[j]:
#             for k in range(i):
#                 if list1[i] == list1[k]:
#                     flag =1
#             if flag == 0:
#                 print(list1[i], end=" ")

# def _sum(_list):
#     sum = 0
#     for i in _list:
#         sum+=i
#     print(sum)
# _sum(list1)

# def _change(_list):
#     for i in range(len(_list)):
#         if _list[i]%2 == 0:
#             _list[i] = 0
# print(list1)
# _change(list1)
# print(list1)

# def foo(_list, elem):
#     for i in _list:
#         if i == elem:
#             return True
#     return False
#
# print(list1)
# print(foo(list1, 7))

# def foo1(_list, elem):
#     count = 0
#     for i in _list:
#         if i == elem:
#             count+=1
#     return count
# print(list1)
# print(foo1(list1, 7))

import random
def creat(size, _min, _max):
    _list=[]
    for i in range(size):
        _list.append(random.randint(_min,_max))
    return _list
list2 = creat(8,10,99)
print(list2)

