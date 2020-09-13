# lists

courses = ['History', 'Math', 'Physics', 'CompSci']

# print(courses)
# print(len(courses))
# print(courses[0])
# print(courses[-1])
print(courses[0:2])  # up to but not including 2
print(courses[:2])  # Same thing

# list methods

# append
courses.append('Art')

# insert
courses.insert(0, 'Design')

courses_2 = ['Art', 'Education']

# insert will add the array into the other array
# courses.insert(0, courses_2)

# Extend will merge or concatenate the arrays
courses.extend(courses_2)
print(courses)
