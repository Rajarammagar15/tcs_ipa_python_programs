class Employee:
    def __init__(self,employee_name,designation,salary,overTimeContribution):
        self.employee_name=employee_name
        self.designation=designation
        self.salary=salary
        self.overTimeContribution=overTimeContribution
        self.overTimeStatus=False

class organization:
    def __init__(self,employee_list):
        self.employee_list=employee_list

    def isEligible(self,overTimeThreshold):
        d={}
        for l in self.employee_list:
            if sum(l.overTimeContribution.values)>=overTimeThreshold:
                Employee.overTimeStatus=True
            d.update({l.employee_name:Employee.overTimeStatus})
        return d

    def totalBonusAmount(self,rate):
        hours=0
        for e,o,n in [self.isEligible(overTimeThreshold).items(),self.employee_list]:
            if o==True:
                hours+=sum(n.overTimeContribution.values)
        total=hours*rate
        return total



if __name__=='__main__':
    n=int(input())
    overTimeContribution={}
    employee_list=[]
    for i in range(n):
        employee_name=input()
        designation=input()
        salary=input()
        m=int(input())
        for j in range(m):
            month=input()
            overTime=int(input())
            overTimeContribution.update({month:overTime})
        employee_list.append(Employee(employee_name,designation,salary,overTimeContribution))
    obj=organization(employee_list)
    overTimeThreshold=int(input())
    rate=int(input())
    for e,o in obj.isEligible(overTimeThreshold).items():
        print(e+' '+o)
    print(obj.totalBonusAmount(rate))

    '''
5
Sunita
Faculty
23000
2
Jan
4
March
6
Arun
Admin
30000
3
Feb
4
March
12
June
10
Dipak
Admin
25000
3
Jan
12
July
5
Aug
3
Balen
HR
12000
3
Jan
12
July
5
Aug
3
Tarun
HR
78000
3
Jan
12
July
5
Aug
3
18
100'''