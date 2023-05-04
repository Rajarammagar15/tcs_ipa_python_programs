'''num=int(input("enter a number: "))
if num%2==0:
    print("even no.")
else:
    print("odd no.")'''



'''string1=input("enter first string: ")
string2=input("enter second string: ")
if string2 == string1:
    print(string2+ " is same as a "+ string1)
else:
    print(string2+ " is not same as a "+ string1)
    if string2 in string1:
        print("but" +string2+ " is a substring of "+ string1)
    else:
        print("and also " +string2+ " is not a substring of "+ string1)'''



'''l=list(map(int,input("enter numbers: ").split()))
while True:
    print("\nHello! user choose your tool\n")
    print("1) add all numbers")
    print("2) find the highest number")
    print("3) find the average of all numbers")
    print("4) find the number with highest frquency in list")
    print("5) for quit!")

    p=int(input("enter your choice:"))

    if p==1:
        add=0
        for num in l:
            add=add+num
        print("sum of all numbers is: " +str(add))
    elif p==2:
        print(max(l))
    elif p==3:
        print(add/len(l))
    elif p==4:
        res=max(set(l),key=l.count)
        print("most frequent number is: "+str(res))
    elif p==5:
        print("thank you!")
        exit()
    else:
        print("enter valid choice!")'''



'''class Student:
    def __init__(self,roll_no,name,marks,std):
        self.roll_no=roll_no
        self.name=name
        self.marks=marks
        self.std=std

    def grade(self):
        add=0
        for mark in marks:
            add+=mark
        per=add/len(marks)
        if per>=80:
            ch='A'
        elif 60<=per<80:
            ch='B'
        elif 40<=per<60:
            ch='C'
        else:
            ch='F'
        return ch


roll_no = int(input("enter a roll numbers: "))
name = input("enter a name of student: ")
std = int(input("enter a standard of student: "))
marks = []
n = int(input("total number of subject: "))
for i in range(n):
    l1 = int(input(f"enter marks of {i+1} subject: "))
    marks.append(l1)
s = Student(roll_no,name,marks,std)
print("grade given to student:" +s.grade())'''



'''def check_string(st):
    special_character="~`!@#$%^&*()_-+=""{[}]|\:;'<,>.?/"
    count_of_valid_string=0
    count_of_invalid_string = 0
    flag=False
    for i in range(len(st)):
        for char in st[i]:
            if (char.isalpha()==True or char.isspace()==True) and char.isdigit()==False and (char in special_character)==False:
                flag=True
            else:
                flag=False
                break

        if flag==True:
            count_of_valid_string += 1
        else:
            count_of_invalid_string += 1
    print(count_of_valid_string)
    print(count_of_invalid_string)

if __name__ == '__main__':
    st=[]
    n=int(input())
    for i in range(n):
        st.append(input())
    check_string(st)'''


class Employee:
    #overTimeStatus = False
    def __init__(self, employeeName, designation, salary, overTimeContribution):
        self.overTimeStatus=False
        self.employeeName = employeeName
        self.designation = designation
        self.salary = salary
        self.overTimeContribution = overTimeContribution

class Organization:
    sel = []
    def __init__(self, employee_list):
        self.employee_list = employee_list
    def is_Eligible(self,th,emp):
        add = sum(emp.overTimeContribution.values())
        if add >= th:
            Employee.overTimeStatus = True
            o.sel.append(add)
            st = str(Employee.overTimeStatus)
            return st
        else:
            Employee.overTimeStatus = False
            st = str(Employee.overTimeStatus)
            return st

    def total_bonus(self,rate):
        return sum(o.sel)*rate

if __name__ == '__main__':
    employee_list = []
    n = int(input())
    for i in range(n):
        employeeName = input()
        designation = input()
        salary = int(input())
        overTimeContribution = {}
        m = int(input())
        for t in range(m):
            keys=input()
            values=int(input())
            overTimeContribution.update({keys:values})
        e = Employee(employeeName,designation,salary,overTimeContribution)
        employee_list.append(e)
    o = Organization(employee_list)
    th=int(input())
    rate=int(input())
    for emp in employee_list:
        print(emp.employeeName+" "+str(o.is_Eligible(th,emp)))
    print(o.total_bonus(rate))

    '''
5
sunita
faculty
23000
2
jan
4
march
6
arun
admin
30000
3
feb
4
march
12
june
10
dipak
admin
25000
3
jan
12
july
5
aug
3
balen
hr
12000
3
jan
12
july
5
aug
3
tarun
hr
78000
3
jan
12
july
5
aug
3
18
100'''