# definim clasele Student and Courses

class Student:
    # definim constructorul clasei
    def __init__(self, name, surname, age, year, grade):
        # atributele studentului cu ajutorul carora vom crea un obiect de tip student
        self.name = name
        self.surname = surname
        self.age = age
        self.year = year # 1 - 4
        self.grade = grade # 1 - 10

    # definim o metoda
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students, duration):
        # definim atributele
        self.name = name
        self.max_students = max_students
        self.duration = 2
        self.students = []

    # cream metoda cu care adaugam studenti la curs
    def add_students(self, student):  # studentul va fi o instanta a clasei student
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False


# cream obiect/instanta a clasei Student (Cream un Student)

student1 = Student("Glassworth", "Lina", 19, 1, 8)  # instanta/obiect a clasei student
student2 = Student("Glass", "Diana", 20, 1, 10)  # instanta/obiect a clasei student
student3 = Student("Worth", "Bogdan", 19, 1, 9)  # instanta/obiect a clasei student

# cream obiect/instanta a clasei Curs (cream un curs)
c1 = Course("Analiza matematica", 7, 2)
c2 = Course("Computer science", 2, 2)

# print name of student 2
print(student2.name)
# print year of student 3
print(student3.year)

# adaugam studentul 1 la cursul 1
c1.add_students(student2)
c1.add_students(student1)

# afiseaza numele primului student dinents[0].name)

# adaugam studentii1,2,3 la c2

c2.add_students(student1)
c2.add_students(student2)
c2.add_students(student3)

# printam studentii din c2
print(c2.students[0].name)
print(c2.students[1].name)
print(c2.students[2].name)

