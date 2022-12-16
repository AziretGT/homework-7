class Name:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f'{self.name}'
    

class Age:
    def __init__(self,age):
        self.age=age

    def __str__(self):
        return f'{self.age}'


class Second:
    def sc_name(self):
        print(f"{self} is running")

class Hp:
    def hp(self):
        print(f"{self} is flying")


class Human(Name,Second,Hp,Age):
    def __init__ (self,name,age):
        Name.__init__(self,name)
        Age.__init__(self,age)

    def __str__(self):
        return f'{self.name},{self.age}'

human=Human("beka",44)
human.sc_name()
human.hp()
# print(human)