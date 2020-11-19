# создание конструктора и деструктора
class Person:
    def __init__(self, name, surname, qualification = 1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    def information(self):
        return ('Name - ' + self.name,
                'Surname - ' + self.surname,
                'Qualification - ' + str(self.qualification))

    def __del__(self):
        text = "Goodbye mr." + self.surname
        print(text)

employee1 = Person('Petro', 'Poroshenko', 3)
employee2 = Person('Volodymyr', 'Zelensky', 2)
employee3 = Person('Victor', 'Yanukovich', 3)

print(employee1.information())
print(employee2.information())
print(employee3.information())

del()

