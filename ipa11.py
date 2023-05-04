class Account:
    def __init__(self,cno,p,b,wa,at):
        self.cardNumber=cno
        self.pin=p
        self.balance=b
        self.withdrawalAmount=wa
        self.accountType=at

    def updateBalance(self,wa):
        if wa<=self.balance:
            self.balance-=wa
            Account.withdrawalAmount=wa
        return self.balance


class ATM:
    def __init__(self,bn,al):
        self.branch_name=bn
        self.accountList=al

    def validate(self,cn,p,wa):
        for i in self.accountList:
            if cn==i.cardNumber and p==i.pin:
                Account.balance=Account.updateBalance(wa)
                return i

    def acc(self,at):
        d={}
        for i in self.accountList:
            if at==i.accountType:
                d[i.cardNumber]=i.balance
        return d

if __name__=='__main__':
    n=int(input())
    al=[]
    for i in range(n):
        cno=int(input())
        p=int(input())
        b=float(input())
        wa=float(input())
        at=input()
        al.append(Account(cno, p, b, wa, at))
    obj=ATM('sbi',al)
    cn=int(input())
    pin=int(input())
    wA=float(input())
    x,y,z=obj.validate(cn, pin, wA)
    if obj.validate(cn, pin, wA)==None:
        print('No account Exist')
    else:
        print(x+' '+y+' '+z)
    aT=input()
    if obj.acc(aT)==None:
        print('No match Found')
    else:
        for k,v in obj.acc(aT).items():
            print(k+':'+v)


'''
2
12345
12
30.0
10.0
salary
45678
98
400.0
200.0
salary
45678
98
100.0'''