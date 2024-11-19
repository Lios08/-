grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [5, 3, 3, 5, 4], [4, 4, 3], [5, 5, 5, 4, 5]]
av= sum (grades[0]) / len (grades[0])
av1= sum (grades[1]) / len(grades[1])
av2= sum (grades[2]) / len(grades[2])
av3= sum (grades[3]) / len(grades[3])
av4= sum (grades[4]) / len(grades[4])
grad = (av, av1, av2, av3, av4)
#print(grad)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
students_dict = dict(zip(sorted_students, grad ))
print(students_dict)

