class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")
person1 = Person("Anil", 23)
person1.introduce()

