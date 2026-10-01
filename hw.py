# h.w (16/6/26)
# 1)
# print([i**2 for i in range(1,21) ])

# 2)
# print([i for i in range(1,21) if i%3==0])

# 3)
# print([i for i in range(1,31) if i%5==0 and i%2==0])

# 4)
# print([i for i in range(1,21) if i%3==0 or i%2==0])


# h.w (17/6/26)

# 1Q)
# students_in_CS_department={'a','b','c','d','e','f'}
# students_in_EC_department={'d','e','f','g','h'}

# a)find students either in CS or EC=
# print(students_in_CS_department ^ students_in_EC_department)
# b)find sstudents in both CS and EC=
# print(students_in_CS_department | students_in_EC_department)
# c)find students only in CS=
# print(students_in_CS_department - students_in_EC_department)
#  d)find students only in EC=
# print( students_in_EC_department - students_in_CS_department)

# 2Q)
python={'a','b','c','d','e'}
java={'b','d','f','g'}

# a) find students who know atleast one language=
print(python | java)
# b)find students bwho know both languages=
print(python & java)
# c)find students bwho know only python=
print(python - java)
# d)find students bwho know only java=
print(java -python)