from models import *

me = Person("Wendell", "Adriel", 25)
me.greeting()

me.first_name = "John"
me.set_last_name("Doe")
me.set_age(40)
me.greeting()

other = Person("Mary", "Smith", 30)
other.greeting()

other.first_name = "Jenna"
other.set_last_name("Jenkins")
other.set_age(20)
other.greeting()

emp = Employee("Peter", "Green", 25, "Developer")
emp.greeting()

emp.first_name = "Dave"
emp.set_last_name("Johnes")
emp.set_age(45)
emp.set_role("Pirate")
emp.greeting()