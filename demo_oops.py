# class Person:
#     name = "vishwas"
#     city = "Bengaluru"

# p1 = Person()
# print(p1.name)
# print(p1.city)

# p2 = Person()
# print(p2.name)
# print(p2.city)


class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city
    
    def display_person(self):
        print(f"Name: {self.name}, City: {self.city}")


class User(Person):
    def __init__(self, name, city, salary):
        super().__init__(name, city)
        self.salary = salary
    
    def display_person(self):
        super().display_person()
        print(f"Salary: {self.salary}")

p1 = Person("vishwas", "Bangalore")
p1.display_person()

p2 = Person("Rita", "Delhi")
p2.display_person()
u1 = User("John", "New York", 20000)
u1.display_person()

p1.location = "India"
print(p1.location)
print(p1.__dict__)