class abc:

    def __init__(self,Name,Age):
            print("constructor calling")
            print("the studend bio deta :")
        
            self.x = Name
            self.y = Age

    def __del__(self):
        print("destructors executed")

obj1 = abc("venkat",25)
print(obj1.x,obj1.y)
del obj1
print("---------------------------")
obj2 = abc("tamil",50)
print(obj2.x,obj2.y)
print("---------------------------")
obj3 = abc("kural",27)
print(obj3.x,obj3.y)
print("---------------------------")
obj4 = abc("jeeva",24)
print(obj4.x,obj4.y)
print("---------------------------")

print("code EnD")