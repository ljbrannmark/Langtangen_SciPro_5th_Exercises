# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 22:51:30 2020

@author: lars-johan.brannmark
"""

class Course(object):
    def __init__(self, title, semester, credit, grade):
        self.title = title
        self.semester = semester
        self.credit = credit
        self.grade = grade

    def __str__(self):
        return '%-40s%-15s%-8s%-8s' %(self.title, self.semester, self.credit, self.grade)
        


class Student(object):
    def __init__(self, name, *courses):
        self.name = name
        self.courses = [courses[i] for i in range(len(courses))]
        
    def __str__(self):
        s = '+'*71 + '\n'
        s += '\nName: %s\n\n' %self.name 
        s += '%-40s%-15s%-8s%-8s\n' %('Course', 'Semester', 'Credit', 'Grade')
        s += '-'*71 + '\n'
        for i in range(len(self.courses)):
            s += str(self.courses[i]) + '\n'
        s += '\n'
        return s
        
    def add_courses(self, *courses):
        courselist = [courses[i] for i in range(len(courses))]
        self.courses += courselist
        
   
        
class Student_Register(object):
    #A Student_Register contains a list of students. Initialization is done 
    #with a list of students, or a single student.
    def __init__(self, students):
        if isinstance(students, Student):
            students = [students]
        self.student_list = [students[i] for i in range(len(students))]
        
    def __str__(self):
        s = ''
        for student in self.student_list:
            s += str(student)
        return s
        
    def load(self, studentfile):
        #Add students to the list by loading data from a text file:
        infile = open(studentfile, 'r')
        students = []
        for line in infile:
            i = line.find('Name:')
            if i != -1:
                # line contains 'Name:', extract the name
                name = line[i+5:]
                name = name.strip()  # strip off blanks
                #Create a new student and append to the list
                s = Student(name)
                students.append(s)
            elif line.isspace():     # blank line?
                continue             # go to next loop iteration
            else:
                # This must be a course line
                words = line.split()
                grade = words[-1]
                credit = int(words[-2])
                semester = ' '.join(words[-4:-2])
                course_name = ' '.join(words[:-4])
                #Create a course object
                c = Course(course_name, semester, credit, grade)
                #Add the course to the latest created student
                students[-1].add_courses(c)
            
        infile.close()
        self.student_list += students
        return None
