# object method(acess)
# class Company:
#     cid=7557
#     cname="QUEST"

#     def __init__(self,cid,cname):
#         self.cid=cid
#         self.cname=cname

#     def display(self):
#         print("EMPLOYEE ID:",self.cid) 
#         print("EMPLOYEE NAME:",self.cname)  

# c1=Company(200,"MANU")         
# c2=Company(210,"ANU") 
# c3=Company(211,"RAJU")

# c1.display()
# c2.display()
# c3.display()

# object method(modify)

# class Company:
#     cid=7557
#     cname="QUEST"

#     def __init__(self,cid,cname):
#         self.cid=cid
#         self.cname=cname

#     def display(self):
#         print("EMPLOYEE ID:",self.cid) 
#         print("EMPLOYEE NAME:",self.cname) 

#     def change(self,new_eid,new_ename):
#           self.cid=new_eid
#           self.cname=new_ename    

# c1=Company(200,"MANU")         
# c2=Company(210,"ANU") 
# c3=Company(211,"RAJU")

# c1.change(300,"MANU")
# c1.display()
# # c2.display()
# # c3.display()



# class method(acess)
# class Company:
#     cid=7557
#     cname="QUEST"

#     def __init__(self,cid,cname):
#         self.cid=cid
#         self.cname=cname

#     def display(self):
#         print("EMPLOYEE ID:",self.cid) 
#         print("EMPLOYEE NAME:",self.cname) 

#     def change(self,new_eid,new_ename):
#           self.cid=new_eid
#           self.cname=new_ename 

#     @classmethod
#     def show(cls):
#         print("COMPANY ID",cls.cid)  
#         print("COMPANY NAME",cls.cname)  


# c1=Company(200,"MANU")         
# c2=Company(210,"ANU") 
# c3=Company(211,"RAJU")

# c1.change(300,"MANU")
# c1.display()
# # c2.display()
# # c3.display()  

# c1.show()   

# class method(modify)
# class Company:
#     cid=7557
#     cname="QUEST"

#     def __init__(self,cid,cname):
#         self.cid=cid
#         self.cname=cname

#     def display(self):
#         print("EMPLOYEE ID:",self.cid) 
#         print("EMPLOYEE NAME:",self.cname) 

#     def change(self,new_eid,new_ename):
#           self.cid=new_eid
#           self.cname=new_ename   
#     @classmethod
#     def show(cls):
#         print("COMPANY ID:",cls.cid)  
#         print("COMPANY NAME:",cls.cname) 
#     @classmethod
#     def modify(cls,new_eid,new_ename):
#         cls.cid=new_eid
#         cls.cname=new_ename   

# c1=Company(200,"MANU")         
# c2=Company(210,"ANU") 
# c3=Company(211,"RAJU")

# c1.change(300,"MANU")
# c1.display()
# # c2.display()
# #  c3.display() 
# c1.show()    
# c3.modify(335,"URT")
# c3.show()

# static method(common)
class Company:
    cid=7557
    cname="QUEST"

    def __init__(self,cid,cname):
        self.cid=cid
        self.cname=cname

    def display(self):
        print("EMPLOYEE ID:",self.cid) 
        print("EMPLOYEE NAME:",self.cname) 

    def change(self,new_eid,new_ename):
          self.cid=new_eid
          self.cname=new_ename   
    @classmethod
    def show(cls):
        print("COMPANY ID:",cls.cid)  
        print("COMPANY NAME:",cls.cname) 
    @classmethod
    def modify(cls,new_eid,new_ename):
        cls.cid=new_eid
        cls.cname=new_ename   

    @staticmethod
    def greet(ename):
        print ("Hello",ename)   

c1=Company(200,"MANU")         
c2=Company(210,"ANU") 
c3=Company(211,"RAJU")

c1.change(300,"MANU")
c1.display()
# c2.display()
#  c3.display() 
c1.show()    
c3.modify(335,"URT")
c3.show()

c1.greet("MANU")