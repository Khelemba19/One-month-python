#WAP to put the grades in a tuple and count how many students got A and then put them in a list and sort them in ascending order
Grades = ('C', 'D', 'A' , 'A' , 'B', 'B' ,'A')
a_count = Grades.count("A")
print("The numbers of students that got 'A': ", a_count)

list_Grades = list(Grades)
list_Grades.sort()
print(list_Grades)