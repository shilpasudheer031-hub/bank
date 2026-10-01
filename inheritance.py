# single level inheritance
# class A:
#     a=10
#     b=90
# class B(A):
#     c=76
#     d=86
# oa=A()  
# ob=B() 
# print(oa.a,oa.b)  
# print(ob.c,ob.d,ob.b,ob.a)   

# constuctor chaning

# class Bank:
#     Bname="SBI"
#     Bloc="TVM"

#     def __init__(self,cname,cbal):
#         self.cname=cname
#         self.cbal=cbal

# class Bank1(Bank):
#     def __init__(self, cname, cbal,cphone,cloc):
#         super().__init__(cname, cbal) 
#         self.cphone=cphone
#         self.cloc=cloc
#     def display(self):
#         print("CUSTOMER NAME",self.cname)           
#         print("CUSTOMER BALANCE",self.cbal)
#         print("CUSTOMER MOBILE",self.cphone)
#         print("CUSTOMER LOCATION",self.cloc)

# c1=Bank1("Anju",8000,8747855643,"Kannur")    
# c2=Bank1("Meenu",46840,7478556439,"Kollam")    

# c1.display()
# c2.display()


# method chaning
# class Bank:
#     Bname="SBI"
#     Bloc="TVM"

#     def __init__(self,cname,cbal):
#         self.cname=cname
#         self.cbal=cbal

#     def display(self):
#         print("CUSTOMER NAME",self.cname)           
#         print("CUSTOMER BALANCE",self.cbal)   

# class Bank1(Bank):
#     def __init__(self, cname, cbal,cphone,cloc):
#         super().__init__(cname, cbal) 
#         self.cphone=cphone
#         self.cloc=cloc
#     def display(self):
#         super().display()
#         print("CUSTOMER MOBILE",self.cphone)
#         print("CUSTOMER LOCATION",self.cloc)

# c1=Bank1("Anju",8000,8747855643,"Kannur")    
# c2=Bank1("Meenu",46840,7478556439,"Kollam")    

# c1.display()
# c2.display()


# multilevel inheritance
class A:
    a=10
    b=90
class B(A):
    c=76
    d=86
class C(B):
    e=97
    f=80    
oa=A()  
ob=B() 
oc=C()
print(oa.a,oa.b)  
print(ob.c,ob.d,ob.b,ob.a)
print(oc.a,oc.b,oc.c,oc.d,oc.e,oc.f)