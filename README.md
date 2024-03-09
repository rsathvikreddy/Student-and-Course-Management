# Student and Course Management
A simple student and course management system using Object Oriented Programming
    
## What to do?
Clone the repository

There are three python files
- main.py
- student.py
- course.py

Run the main.py

## what is in ```main.py```?
The main.py file imports classes and methods from student.py and course.py
```python
from student import Student
from course import Course
```
The menu is navigated by selecting the number, the ```while True``` loop is used so that the menu goes on unless we  hit exit

```python
while True:
      print(f'''  
x----------------------x----------------------x
            
            Enter a number between 1 - 11 

      1. Add Student
      2. Add Course
      3. Add Student to a Course
      4. Remove Student from the Course
      5. Add Marks/Update Marks
      6. Student Information
      7. Update Student's Information
      8. Remove Student
      9. Course Information
      10.Remove Course
      11.Exit
      
      Number of students = {len(Student.students)}
      Number of courses = {len(Course.courses)}

x----------------------x----------------------x
      ''')
```

We take input via a custom function ```validateinput``` which is used so that the user must have to type a input and can't input a NULL value or incorrect data type. We use ```.strip()``` to remove the whitespaces in starting and the end. We use try and except ```ValueError``` which strikes when the input of an 'int' datatype input is NULL. We use ```len()==0``` so that the 'str' datatype input wont be NULL.

validateinput(sentence,```data = str```), data = str because we don't have to explicity mention 'str' datatype often

```
def validateinput(sentence,data = str): 
      while(True):
            try:
                  user = data(input(sentence))
                  if data == str:
                        user = user.strip()
                        if(len(user) == 0):
                              print("Enter a valid input")
                              continue
            except ValueError:
                  print("Enter a valid input")
                  continue
            else:
                  return user
```
## What is in ```student.py```?
The student.py file contains the class ```Student``` which is used to create student instances/objects of the students. 

The constructor intakes 5 attributes for student
```
def __init__(self,name,age,ID,mail,Phone_number):
```

```students = []``` contains the instances of the students

```self.clist ={}``` contains each students course name and GPA

The Student class contains three methods 
 - check ()
 - studentinfo()
 - update()

```check()``` method is used to check if a student has a particular course, this method is used in option 5 (Add/Update Marks)

```studentinfo()``` method is used to display the student's Information and also calculate student's CGPA by taking the average of each course's GPA

```update()``` method is used update student's information 

## What is in ```course.py```?
The course.py file contains the class ```Course``` which is used to create course instances/objects of the courses and also it imports Student class from student.py 

The constructor intakes 3 attributes for course
```
def __init__(self,cname,ccode,credits):
```
```courses = []``` contains the instances of the courses

```self.estudents = []``` contains each course's enrolled students

The Course class contains six methods
- addStudent() - Adds exisiting student into a course 
- courseinfo() - To display course's information and also calculates average GPA of the course by iterating through clist{ } and estudents[ ]
- removeStudentfromCourse() - Removes Student from a course
- removecourse() - Removes/Deletes the course
- removeStudent() - Removes/Deletes the Student
- addMarks() - Adds marks of the students (considering three tests and one project) and averages them to get GPA of that student in that particular course

***Note :*** ```Flag, Flag1, Flag2``` these keywords are used often to check which value is missing from the list (student or course)

# Let's run it !!!!
I had done a testrun and recorded it 

https://drive.google.com/file/d/1DCkSiFq8uk2LCkjrpSqx91j69IXdQstC/view?usp=drive_link

Thank you!!!
