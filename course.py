from student import Student
class Course(Student):
    
    courses = [] #objects
    

    def __init__(self,cname,ccode,credits):
        self.cname = cname
        self.ccode = ccode
        self.credits = credits
        self.estudents = []
        gpa = 0
        
        

    @classmethod
    def addStudent(self,id,course):
        print("\n")
        flag = 0
        flag2 = 0
        for k in Course.courses:
            if k.cname == course:
                for x in k.estudents:
                    if x.ID == id:
                        print("Student already added into the course") 
                        return
        for i in Student.students:
            if i.ID == id:
                flag = 1
                for j in Course.courses:
                    if j.cname == course:
                        flag2 = 1
                        j.estudents.append(i)
                        i.clist[j.cname] = 0
                        print(f"{id} has been added into {course}")
                        break
                break
        if(flag == 0 or flag2 == 0):
            print("Student or Course not found")
              

    @classmethod
    def courseinfo(self,name):
        flag = 0
        for i in Course.courses:
            if i.cname == name:
                flag = 1
                print(f"Course Name : {name}")
                print(f"Course Code : {i.ccode}")
                print(f"Course Credits : {i.credits}")
                print(f"Number of Students Enrolled : {len(i.estudents)}")
                avggpa = 0
                for sum in i.estudents:
                    avggpa += sum.clist[name]
                if(len(i.estudents) == 0):
                    print(f"Average GPA : 0")
                else:
                    print(f"Average GPA : {avggpa/len(i.estudents)}")
        if flag == 0:
            print("Course not found")


    @classmethod
    def removeStudentfromCourse(self,id,course):
        flag = 0
        flag1 = 0
        flag2 = 0
        for j in Student.students:
            if j.ID == id:
                flag = 1
        for i in Course.courses:
            if i.cname == course:
                flag1 = 1
                for k in i.estudents:
                    if k.ID == id:
                        flag2 = 1
                        i.estudents.remove(k)
                        k.clist.pop(course)
                        print(f"{id} has been removed from {course}")
                        return
                break
        if(flag == 0 and flag1 == 0):
            print("Course and Student doesnt exist")
        elif flag1 == 0:
            print("Course doesnt exist")
        elif flag == 0:
            print("Student doesnt exist")
        elif flag2 == 0:
            print("Student is not alloted to this Course in the first place")


    @classmethod
    def removecourse(self,name):
        flag = 0
        for i in Course.courses:
            if i.cname == name:
                flag = 1
                for k in i.estudents:
                    k.clist.pop(name)
                Course.courses.remove(i)
                print(f"{name} course has been removed")
                break
        if (flag == 0):
            print("Course not found")


    @classmethod
    def addMarks(self,marks,id,course):
        for i in Course.courses:
            if i.cname == course:
                for j in i.estudents:
                    if j.ID == id:
                        j.clist[course] = sum(marks) / 10
                        break

    @classmethod
    def removeStudent(self,id):
        for i in Student.students:
            flag = 0
            if i.ID == id:
                for k in i.clist:
                    for j in Course.courses:
                        if j.cname == k:
                            j.estudents.remove(i)
                            
                (Student.students).remove(i)
                print("Student has been removed")
                flag = 1
                break
        if(flag == 0):
            print("Student not found")
