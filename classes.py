class calculator:
    def addition(x,y):
        added = x+y
        print(added)
    def subtraction(x,y):
        sub = x-y
        print(sub)
    def multiplication(x,y):
        mult = x*y
        print(mult)
    def division(x,y):
        div = x/y
        print(div)


calculator.multiplication(3,5)
calculator.subtraction(1,2)


class Person:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.Pos = []
    def Declare(self, name):
        print(name, "is a new person!")
    def NewPos(self, Pos):
        self.Pos.insert(0,Pos)
        
Pat = Person()
Pat.Declare("Pat")
print("x", Pat.x)

Pat.NewPos((0,0))
Pat.NewPos((1,1))
print("Pat's pos: ", Pat.Pos[0])
print("Pat's last pos: ", Pat.Pos[1])

People = [Person() for i in range(5)]
##People[1] = Person()


def scriptTest(): # can call a funtcion like this just with scriptTest()
    print('worked?')

