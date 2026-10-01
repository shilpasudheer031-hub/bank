# multilevel inheritance
# class Details:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print("Name:",self.name) 
#         print("Age:",self.age)   

# class Education(Details):
#     def __init__(self,name,age,degree):
#         super().__init__(name,age)
#         self.degree=degree

#     def display(self):
#         super().display()  
#         print("Degree:",self.degree)  

# class Bio(Education):
#     def __init__(self, name, age, degree,cname,exp):
#         super().__init__(name, age, degree)
#         self.cname=cname
#         self.exp=exp

#     def display(self) :
#          super().display()
#          print("Company Name:",self.cname) 
#          print("Experience:",self.exp)
               
# person=Bio("Anu",34,"Bsc","Quest",3)
# person.display()
    

# multiple inheritance
# class Details:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display1(self):
#         print("Name:",self.name) 
#         print("Age:",self.age) 

# class Education:
#     def __init__(self,degree):
#         self.degree=degree

#     def  display2(self) :
#         print("Degree:",self.degree) 

# class Biodata(Details,Education):
#     def __init__(self, name, age,degree,cname,exp):
#         Details.__init__(self,name,age)
#         Education.__init__(self,degree)
#         self.cname=cname
#         self.exp=exp

#     def display(self):
#         super().display1() 
#         super().display2()   
#         print("Company Name:",self.cname) 
#         print("Experience:",self.exp)
               
# person=Biodata("Anu",34,"Bsc","Quest",3)
# person.display()
                
# Hierachial inheritance   
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self) :  
#         print("Name:",self.name) 
#         print("Age:",self.age)

# class Manager(Person):
#     def __init__(self,name,age,mgid):
#             super().__init__(name,age)
#             self.mgid=mgid

#     def display(self):
#               print("Managerid",self.mgid)
#               super().display()   

# class Employee(Person):
#      def __init__(self, name, age,empid):
#           super().__init__(name, age)   
#           self.empid=empid

#      def display(self):
#           print("Employeeid:",self.empid)
#           super().display()   

# m1=Manager("Rahul",24,204)
# e1=Employee("Anju",23,124)

# m1.display()
# e1.display()

# hybrid inheritance
# class Add():
#     def add(self,a,b):
#         print(a+b)

# class Sub():
#     def sub(self,a,b):
#         print(a-b)
        
# class New(Add,Sub):
#     def mul(self,a,b):
#         print(a*b)

# class Calculator(New):
#     def div(self,a,b):
#         print(a/b)

# c1=Calculator()  
# c1.add(5,3) 
# c1.sub(5,3)  
# c1.mul(5,3)  
# c1.div(5,3)       

# # abstraction
# # from abc import ABC,abstractmethod
# # class Sample(ABC):
# #     @abstractmethod
# #     def msg():
#         pass

# class Sample1(Sample)  :
#     def msg(self):
#         print("helooooo")

# S1.Sample1() 
# S1.msg()      



from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def checkbalance():
        pass
    @abstractmethod
    def withdraw():
        pass
    @abstractmethod
    def deposit():
        pass




class AXIS(ATM):
    def __init__(self,cname,cbal,cpin):
        self.cname=cname
        self.cbal=cbal
        self.cpin=cpin

    def checkbalance(self):
        pin=int(input("Enter pin:")) 
        if pin==self.cpin:
            print("Balance:",self.cbal) 
        else:
            print("Incorrect pin")  

    def withdraw(self):
        pin=int(input("Enter pin:")) 
        if pin==self.cpin:
            amt=int(input("Enter amount:"))
            if amt<=self.cbal:
                self.cbal=self.sub(self.cbal,amt)
                print("Avaliable balance:",self.cbal)
            else:
                print("Insuffient balance") 
        else:
            print("Incorrect pin")  

    def  deposit(self):
        pin=int(input("Enter pin:")) 
        if pin==self.cpin:
            amt=int(input("Enter amount:"))
            self.cbal=self.add(self.cbal,amt)
            print("Avaliable balance:",self.cbal)
             
        else:
            print("Incorrect pin")  

    @staticmethod
    def add(a,b):
        return a+b      

    def sub(a,b):
        return a-b  

c1=AXIS("riya",6000,234)
c2=AXIS("anju",5000,456)


c1.checkbalance()
c1.deposit()
c2.withdraw()
           