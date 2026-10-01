# username="abc"
# password="abc123"
# user=input("enter your user:")
# if user==username:
#     password1=input("enter password:")
#     if password==password1:
#         print("login sucessfully....")
#     else:
#         print("incorrect password")    
# else:
#     print("username not found")      


# x=int(input("x co-ordinate ="))
# y=int(input("y co-ordinate ="))
# if x>0 and y>0:
#     print("allpositive")
# elif x<0 and y>0:
#     print("x is nagative and y is positive") 
# elif x<0 and y<0:
#     print("allnegative")
# elif x>0 and y<0:
#     print("x is positive and y is negative") 
# elif x==0 and y==0:
#     print("origin")
# else:
#     print("axis")    


# while Loop

# (Q) find a sum of first 5 natural numbers

# i=1
# sum=0
# while i<=5:
#     sum=sum+i
#     i=i+1
# print(sum)   
# 
#  (Q) find a sum of first n natural numbers
# i=1
# sum=0
# n=int(input("enter a number:"))
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum)

# (Q) find a factorial
# i=1
# fact=1
# while i<=4:
#     fact=fact*i
#     i=i+1
# print(fact)  
# 
# (Q)find a reverse of a number  
# n=int(input("enter a number:"))
# rev=0
# while n>0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# print(rev)  
# 
# (Q) check a number is palindrome
# n=int(input("enter a number:"))
# tem=n
# rev=0
# while n>0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# if tem==rev:
#     print("palindrome") 
# else:
#     print("not a palindrome")     
#   
# (Q) sum of list on elements
# s=[1,3,4]
# i=0
# sum=0
# while i<len(s):
#     sum=sum+s[i]
#     i=i+1
# print(sum)  
# 
# (Q)  find a prime number
# n=int(input("enter a number:"))
# i=2
# while i<n:
#     if n%i==0:
#         print("not a prime")
#         break
#     i=i+1
# else:
#     print("prime")    
# (Q) check amstrong number
a=int(input("enter num:"))
temp=a
s=0
pow=len(str(a))
while a>0:
    ld=a%10
    s=s+(ld**pow)
    a=a//10
if s==temp:
    print("amstrong")    
else:
    print("not amstrong")    
