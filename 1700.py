from collections import deque
from typing import Deque

"""
    1 <= students.length, sandwiches.length <= 100
    students.length == sandwiches.length
    sandwiches[i] is 0 or 1.
    students[i] is 0 or 1.
"""
#NOTE:
def countStudents(students, sandwiches):
    s, q = sandwiches, Deque(students)
    taken = True
    while True:
        taken = False # we have not had someone eat a sand yet

        # for each of the students
        for i in range(len(q)):
            currentStudent = q.pop()
            if currentStudent == s[0]:
                taken = True # we took something
                s.pop(0) # remove this sandwhich
            else:
                q.appendleft(currentStudent)

        # if we looked at all students and none of them ate a sandwhich, return this
        if not taken or (len(s) == 0):
            return len(q)
            
    

#Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
#Expected Output: 3
print(countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))

# Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
# Output: 0 
print(countStudents([1,1,0,0], [0,1,0,1]))