class Person(object):
    
    def __init__(self, first, last, age):
        self.first_name = first # Public
        self._last_name = last # Protected
        self.__age = age # Private
    
    def set_last_name(self, last):
        self._last_name = last
    
    def get_last_name(self):
        return self._last_name

    def set_age(self, age):
        self.__age = age
    
    def get_age(self):
        return self.__age

    def greeting(self):
        print("Hello. I'm %s %s and I'm %d years old." % (self.first_name, self._last_name, self.__age))

class Employee(Person):

    def __init__(self, first, last, age, role):
        super().__init__(first, last, age)
        self.__role = role

    def set_role(self, role):
        self.__role = role

    def get_role(self):
        return self.__role

    def greeting(self):
        print("Hello. I'm %s %s and work as a %s." % (self.first_name, self._last_name, self.__role))