# protected without inherit
# class Company:
#     _cname="TCS"
#     def __init__(self,id,ename):
#         self.id=id
#         self.ename=ename

#     def _display(self):
#         print("ID:",self.id)   
#         print("Name:",self.ename)

# e1=Company(101,"Diya")
# # print(e1.cname)
# print(e1._cname)
# # e1.display()
# e1._display() 




# protected with inherit
# class Company:
#     _cname="TCS"
#     def __init__(self,id,ename):
#         self.id=id
#         self.ename=ename

    # def _display(self):
    #     print("ID:",self.id)   
    #     print("Name:",self.ename) 
# class Department(Company) :
#     dept_name="IT"
#     def __init__(self, id, ename,cname):
#         super().__init__(id, ename) 
#         self.cname=cname
#     def display(self):
#         print("Company Name:",self._cname)
                 

# e1=Company(101,"Priya")        
# d1=Department(101,"Priya")
# d1.display()
# print(e1.cname)
# print(e1._cname)
# e1.display()
# e1._display()  



# private acess specifier
# class Parent:
#     def __init__(self):
#         self.__name="Priya"
# class Child(Parent):
#     def display(self):
#         # print("Name:",self.__name) 
#         print("Name:",self._Parent__name) 

# # p1=Parent()
# # p1.display()             
# c1=Child()
# c1.display()  


# append()
f=open('test2.txt','a')
f.write('Have a nice day')
f.close()


f=open('test2.txt','a')
f.write('Good morning')
f.close()

f=open('test2.txt','a')
f.writelines(['hello\n','how\n','are\n','you'])
f.close()