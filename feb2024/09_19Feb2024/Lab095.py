# Class & Objects in Python
# Class -  Attributes and Behaviour

# Person -> Object Vani, Pramod, Shreeram

class Person:
    # Attributes  -> Data members
    name = None
    age = None
    id = None
    phone_no = None

    # Behaviour -> Methods (not the functions)
    def talk(self):
        print("I cam talk")

    def another(self):
        print("I am a Method")

    def sleep(self, name):
        print("I am a Method!!")
        print("Sleep", name)

    def walk(self):
        return "I am walking"


def anotherf():
    print("I am f(n)")


# Objects - ClassName()
shreeram = Person()
# shreeram.name = "Sheeram"
# print(shreeram.name)
# shreeram.talk()  # This belong Shreeram
shreeram.sleep("shreem")
# print(shreeram.walk())



# pramod = Person()
# pramod.age = "99"
# print(pramod.age)
# pramod.sleep(pramod)
#
#
#
# amit = Person()
# amit.id = 112233
# print(amit.id)
# nOTHIGN SI THERE, SO CLEAN THE MEMEMORY
# exit the program