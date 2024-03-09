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

class Student:
    students = []


    def __init__(self,name,age,ID,mail,Phone_number):
        self.ID = ID
        self.name = name
        self.age = age
        self.mail = mail
        self.Phone_number = Phone_number
        self.clist = {}

    def check(id,course):
        flag = 0
        flag2 = 0
        for check in Student.students:
                  if check.ID == id:
                        for key in check.clist:
                              if key == course:
                                   return True
        return False
    
    @classmethod
    def studentinfo(self,id):
        flag = 0
        sumofmarks = 0
        for i in Student.students:
            if i.ID == id:
                flag = 1
                print(f"Name : {i.name}")
                print(f"Age : {i.age}")
                print(f"Mail : {i.mail}")
                print(f"ID : {i.ID}")
                print(f"Phone Number : {i.Phone_number}")
                print(f"Number of Courses Enrolled : {len(i.clist)}")
                if (len(i.clist) == 0):
                    break
                print("Course   :   GPA")
                for key in i.clist:
                    sumofmarks += i.clist[key]
                    print(f"{key}        :   {i.clist[key]}")
                
                print(f"CGPA = {sumofmarks/len(i.clist)}")
        if(flag == 0):
            print("Student not found")

    def update():
        if(len(Student.students) == 0):
             return print("No students found")
        sid = validateinput("Enter Student ID : ")
        for i in Student.students:
            if i.ID == sid:
                print(''' 
                      Enter a number between 1-5
                    1. Update Name 
                    2. Update Age
                    3. Update mail
                    4. Update ID
                    5. Update number  
                    ''')
                option = validateinput("Enter a number ",int)
                if(option == 1):
                    uname = input("Enter updated name : ")
                    i.name = uname
                if(option == 2):
                    uage = input("Enter updated Age : ")
                    i.age = uage
                if(option == 3):
                    umail = input("Enter updated mail : ")
                    i.mail = umail
                if(option == 4):
                     uid = input("Enter updated ID : ")
                     i.ID  = uid
                if(option == 5):
                     uphoneno = input("Enter updated Phone Number : ")
                     i.Phone_number = uphoneno
                break
        print("Student doesnt exist")
                