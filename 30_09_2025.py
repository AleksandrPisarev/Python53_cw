number=int(input('Введите число'))
begin_range1=int(input('Введите начало первого диапазона'))
end_range1=int(input('Введите конец первого диапазона'))
begin_range2=int(input('Введите начало второго диапазона'))
end_range2=int(input('Введите конец второго диапазона'))
begin_range3=int(input('Введите начало третьего диапазона'))
end_range3=int(input('Введите конец третьего диапазона'))
flag=0
count=0
if begin_range1<=number<=end_range1:
    print(f'число {number} принадлежит первому диапазону')
    flag=1
    count+=1
if begin_range2<=number<=end_range2:
    print(f'число {number} принадлежит второму диапазону')
    flag=1
    count+=1
if begin_range3<=number<=end_range3:
    print(f'число {number} принадлежит третьему диапазону')
    flag=1
    count+=1
if flag==0:
    print(f'число {number} не принадлежит  ни одному диапазону')
else: print(f'число {number} принадлежит {count} диапазонам')
#