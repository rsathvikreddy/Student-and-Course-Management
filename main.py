from student import Student
from course import Course
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

      option = validateinput("Enter a number : ",int)
      print("\n")
      if(option > 11):
            print("Enter a valid Input")

      if(option == 11):
            print("Thank you!!")
            break
      
      
      elif(option == 1):
            name = validateinput("Enter Name : ")
            age = validateinput("Enter age : ",int)
            id = validateinput("Enter ID : ")
            mail = validateinput("Enter mail : ")
            number = validateinput("Enter Phone number : ",int)
            for i in Student.students:
                  if(id == i.ID):
                        print("\nID Already exists")
                        break
            Student.students.append(Student(name,age,id,mail,number))


      elif(option == 2):
            cname = validateinput("Enter course name : ")
            ccode = validateinput("Enter the course code : ")
            credits = validateinput("Enter the number of credits : ",int)
            Course.courses.append(Course(cname,ccode,credits))


      elif(option == 3):
            if(len(Student.students) == 0) or (len(Course.courses) == 0):
                  print("Minimum number of students or courses not satisfied")
                  continue
            id = validateinput("Enter student ID : ")
            course = validateinput("Enter course name : ")
            Course.addStudent(id,course)


      elif(option == 4):
            if(len(Student.students) == 0) or (len(Course.courses) == 0):
                  print("Minimum number of students or courses not satisfied")
                  continue
            id = validateinput("Enter student ID : ")
            course = validateinput("Enter course name : ")
            Course.removeStudentfromCourse(name,course)


      elif(option == 5):
            if(len(Student.students) == 0) or (len(Course.courses) == 0):
                  print("Minimum number of students or courses not satisfied")
                  continue
            marks = []
            id = validateinput("Enter student ID : ")
            course = validateinput("Enter course name : ")
            inspect = Student.check(id,course)
            if(inspect):
                  print("Enter marks : ")
                  for i in range(0,3):
                        marks.append(int(input(f"Enter Minor {i+1} marks (/30): ")))
                  marks.append(validateinput("Enter Project Marks (/10): ",int))
                  Course.addMarks(marks,id,course)
            else:
                  print("Student and Course are not valid to add marks")

                                    
      elif(option == 6):
            if(len(Student.students) == 0):
                  print("No Students found")
                  continue
            id = validateinput("Enter Student ID : ")
            Course.studentinfo(id)


      elif(option == 7):
            Student.update()


      elif(option == 8):
            if(len(Student.students) == 0):
                  print("No Students found")
                  continue
            id = validateinput("Enter Student ID : ")
            Course.removeStudent(id)
      

      elif(option == 9):
            if(len(Course.courses) == 0):
                  print("No courses found")
                  continue
            name = validateinput("Enter course name : ")
            Course.courseinfo(name)
      

      elif(option == 10):
            if(len(Course.courses) == 0):
                  print("No courses found")
                  continue
            name = validateinput("Enter Course Name : ")
            Course.removecourse(name)

      

      