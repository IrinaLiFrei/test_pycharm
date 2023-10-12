# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Др. предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать ср. балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
#
# Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.
# Математика,Физика,История,Литература

# Создайте класс Student, который будет представлять студента и его успехи по предметам.
# Класс должен иметь следующие методы:
# __init__(self, name, subjects_file): конструктор класса, принимающий ФИО студента и имя файла с данными
# о предметах и оценках.
# add_subject(self, subject, grade, test_score): метод для добавления информации о предмете, оценке и результате теста.
# get_average_grade(self): метод, возвращающий средний балл студента по всем предметам.
# get_subjects(self): метод, возвращающий список всех предметов, по которым есть информация у студента.
# Реализовать функцию get_average_grades(students), которая принимает список студентов и выводит информацию
# о средних баллах для каждого студента.
# Реализовать функцию get_subject_average(students, subject), которая принимает список студентов и название предмета,
# и выводит информацию о среднем балле по этому предмету для каждого студента.
# Реализовать функцию get_top_student(students, subject), которая принимает список студентов и название предмета,
# и выводит информацию о студенте с наивысшим средним баллом по этому предмету.

import csv


class Range:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        setattr(instance, self.param_name, self._validate(value))

    def _validate(self, value: int):
        if not isinstance(value, int):
            raise TypeError(f'Score must be a number between {self.min_value} and {self.max_value}')
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f'Score must be a number between {self.min_value} and {self.max_value}')
        return value


class Name:
    def __init__(self):
        self.name = None

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        setattr(instance, self.param_name, self._validate(value))

    def _validate(self, name: str):
        for item in name.split():
            if not item.isalpha():
                raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
            if not item.istitle():
                raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        return name


class Student:
    name = Name()
    score = Range(2, 5)
    test_score = Range(0, 100)

    def __init__(self, name: str, subjects_file: str):
        self.name = name
        self.subjects = {}
        self.subjects_file = subjects_file
        with open(subjects_file, 'r', encoding='utf-8') as file:
            lines = csv.reader(file, dialect='excel-tab', delimiter=',')
            for line in lines:
                for item in line:
                    self.subjects[item] = {'grade': [], 'test_score': []}

    def add_subject(self, subject, grade, test_score):
        if subject in self.subjects:
            self.subjects[subject]['grade'].append(grade)
            self.subjects[subject]['test_score'].append(test_score)
        else:
            raise ValueError(f'Предмет {subject} не найден')

    def get_average_grade(self):
        sum_ = 0
        count = 0
        for subj in self.subjects:
            for grade in self.subjects[subj]['grade']:
                if grade != 0 and grade is not None:
                    sum_ += grade
                    count += 1
        return sum_ / count if count != 0 else 0

    def get_average_test_score(self, subject):
        sum_ = 0
        count = 0
        if subject in self.subjects.keys():
            if len(self.subjects[subject]['test_score']) > 0:
                for grade in self.subjects[subject]['test_score']:
                    if grade != 0 and grade is not None:
                        sum_ += grade
                        count += 1
                return sum_ / count
        else:
            raise ValueError(f'Предмет {subject} не найден')

    def get_average_grade_in_subject(self, subject: str):
        sum_ = 0
        count = 0
        if subject in self.subjects.keys():
            if len(self.subjects[subject]['grade']) > 0:
                for item in self.subjects[subject]['grade']:
                    sum_ += item
                    count += 1
                return sum_ / count
        else:
            raise ValueError(f'Предмет {subject} не найден')

    def get_subjects(self):
        subj_list = []
        for key in self.subjects.keys():
            if len(self.subjects[key]['grade']) > 0 or len(self.subjects[key]['test_score']) > 0:
                subj_list.append(key)
        return subj_list

    @staticmethod
    def get_average_grades(students: list):
        for stud in students:
            if not isinstance(stud, Student):
                raise TypeError('Not instance')
            else:
                return f'Average grade of {stud.name}: {stud.get_average_grade()}'

    @staticmethod
    def get_subject_average(students: list, subject: str):
        for stud in students:
            if not isinstance(stud, Student):
                raise TypeError('Not instance')
            else:
                return (f'Average grade of {stud.name} in {subject}:'
                        f' {stud.get_average_grade_in_subject(subject)}')

    def add_grade(self, subject, grade):
        self.subjects[subject]['grade'].append(grade)

    def add_test_score(self, subject, test_score):
        self.subjects[subject]['test_score'].append(test_score)

    @staticmethod
    def get_top_student(students, subject):
        top = ''
        max_grade = 0
        for stud in students:
            if not isinstance(stud, Student):
                raise TypeError('Not instance')
            else:
                if stud.get_average_grade_in_subject(subject) > max_grade:
                    max_grade = stud.get_average_grade_in_subject(subject)
                    top = stud.name
        return f'Best student in {subject} is {top} with average grade: {max_grade}'

    def __str__(self):
        return f'Студент: {self.name}\nПредметы: {", ".join(self.get_subjects())}'


student = Student("Иван Иванов", "subjects.csv")
print(student.get_average_grade_in_subject('История'))

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)
