# single inheritannce
# constuctor chaning
# class Bank:
#     Bname="KGB"
#     Bloc="Kannur"
#     def __init__(self,cname,cbal):
#         self.cname=cname
#         self.cbal=cbal
    
# class Bank1(Bank):
#     def __init__(self, cname, cbal,cph,chouseno):
#         super().__init__(cname, cbal)
#         self.cph=cph
#         self.chouseno=chouseno
#     def display(self):
#         print("CUSTOMER NAME:",self.cname)
#         print("CUSTOMER BALANCE:",self.cbal)
#         print("CUSTOMER PHONE NO:",self.cph)
#         print("CUSTOMER HOUSE NO:",self.chouseno)  

# c1=Bank1("Anju",6000,9886045629,103)        
# c1.display()


# method chaning
# class Bank:
#     Bname="KGB"
#     Bloc="Kannur"
#     def __init__(self,cname,cbal):
#         self.cname=cname
#         self.cbal=cbal
#     def display(self):
#         print("CUSTOMER NAME:",self.cname)
#         print("CUSTOMER BALANCE:",self.cbal)    
    
# class Bank1(Bank):
#     def __init__(self, cname, cbal,cph,chouseno):
#         super().__init__(cname, cbal)
#         self.cph=cph
#         self.chouseno=chouseno
#     def display(self):
#         super().display()
#         print("CUSTOMER PHONE NO:",self.cph)
#         print("CUSTOMER HOUSE NO:",self.chouseno)  

# c1=Bank1("Anju",6000,9886045629,103)        
# c1.display()   

# multilevel inheritance

class Bank:
    Bname="KGB"
    Bloc="Kannur"
    def __init__(self,cname,cbal):
        self.cname=cname
        self.cbal=cbal
    def display(self):
        print("CUSTOMER NAME:",self.cname)
        print("CUSTOMER BALANCE:",self.cbal)    
    
class Bank1(Bank):
    def __init__(self, cname, cbal,cph):
        super().__init__(cname, cbal)
        self.cph=cph
        # self.chouseno=chouseno
    def display(self):
        super().display()
        print("CUSTOMER PHONE NO:",self.cph)
         
class Bank2(Bank1) :
    def __init__(self, cname, cbal, cph,chouseno):
        super().__init__(cname, cbal, cph)  
        self.chouseno=chouseno
    def display(self):
        super().display()
        rint("CUSTOMER HOUSE NO:",self.chouseno)



c1=Bank1("Anju",6000,9886045629,103)        
c1.display()   