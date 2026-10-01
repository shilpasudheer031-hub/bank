# slicing
m="good morning"
print(m[0:4])
print(m[0:4:2])
print(m[:4])
print(m[-7:])
print(m[-12:-8])
print(m[:12:2])
print(m[::2])
print(m[1::2])
print(m[::-1])

# palindrome
m=input("enter str:")
if m==m[::-1]:
    print("palindrome")
else:
    print("not palindrome")    

# string methods
text="i love python"
print("text.title()")

text1="Python Is Fun"
text2="python is fun"
print(text1.istitle())
print(text2.istitle())

text3="hello world"
print(text3.capitalize())

s="python programing language"
print(s.startswith('r',8,26))
print(s.startswith('p'))
print(s.endswith('o',2,5))

sh="PYTHON"
sr="python"
print(sh.lower())
print(sh.islower())
print(sr.islower())
print(sr.upper())
print(sh.isupper())
print(sr.isupper())
print(sh.casefold())

sl="pYtHoN"
print(sl.swapcase())

print(s.find('y'))
print(s.find('o',7,11))
print(s.rfind('y'))
print(s.index('y'))
print(s.rindex('o',7,11))


ds="abgfth"
print(ds.isalpha())

dd="fth346"
print(dd.isalnum())
