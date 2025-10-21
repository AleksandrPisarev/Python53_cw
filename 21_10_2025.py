jornal = []
# for i in range(3):
#     for j in range(4):
#         print(students[i][j], end=" ")
#     print()

# sum = 0
# for i in range(len(students)):
#     sum+=students[1][i]
# print(sum/3)


subject = ["рус", "мат", "лит", "физ"]
def add_subject(subject_name):
    subject_name = subject_name[:3]
    subject.append(subject_name)
    for i in range(len(jornal)):
        jornal[i].append(0)

def add_student():
    jornal.append([])
    for i in subject:
        jornal[len(jornal)-1].append(0)

def filling_jornal(student, subject, grade):
    index = subject.index(subject)
    jornal[student-1][index+1] = grade

def del_student(student):
    jornal.remove(jornal[student-1])

def del_subject(subject):
    subject.remove(subject)
    for i in range(len(jornal)):
        jornal[i].pop()

def start_menu():
    variant = int(input(
        '''
        1. вывод журнала
        2. добавление студента
        3. добавление дисциплины
        4. удаление студента
        5. удаление дисциплины
        6. замена оценки
        7. выход
        '''
    ))
    match variant:
        case 1: show_jornaj()
        case 2: add_student()
        case 3: add_subject(input('Введите дисциплину: '))
        case 4: del_student(int(input('Введите номер студента: ')))
        case 5: del_subject(input('Введите дисциплину: '))
        case 6:
            student = int(input('Введите номер студента: '))
            subject = input('Введите предмет: ')
            grade = int(input('Введите оценку: '))
            filling_jornal(student,subject,grade)
        case 7: exit()


def show_jornaj():
    print("№", end="")
    for i in subject:
        print(f"\t| {i}", end="")
    print()
    for i in range(len(jornal)):
        print(i+1, end="\t")
        for j in range(len(jornal[i])):
            print("| ", jornal[i][j], end="\t")
        print()

if __name__ == '__main__':
   while True:
       start_menu()
