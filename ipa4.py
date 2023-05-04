class Account:

    def __init__(self, cardNumber, pin, balance, withdrawalAmount, accountType):
        self.cn = cardNumber
        self.p = pin
        self.b = balance
        self.wa = withdrawalAmount
        self.at = accountType

    def updat(self, wa):
        self.wa=wa
        if wa <= self.b:
            return (self.b-wa)

class ATM:
    def __init__(self, branch_name, accountList):
        self.bn=branch_name
        self.al=accountList

    def withdraw(self, card_number, pin, withdrawalAmount):
        w=withdrawalAmount
        for i in self.al:
            if card_number==i.cn and pin==i.p:
                return a.updat(a,w)

    def filter(self, accountType):
        d = {}
        for i in self.al:
            if i.at == accountType:
                d.update({i.cn, i.b})
        return d


accountList=[]
a = Account
n = int(input())
for i in range(n):
    cardNumber=int(input())
    pin=int(input())
    balance=float(input())
    withdrawalAmount=float(input())
    accountType=input()
    accountList.append(a(cardNumber,pin,balance,withdrawalAmount,accountType))
atm=ATM('sbi',accountList)
cardNumber=int(input())
pin=int(input())
withdrawalAmount=float(input())
balance=atm.withdraw(cardNumber,pin,withdrawalAmount)
print(str(cardNumber)+' '+str(balance)+' '+str(withdrawalAmount))
accountType=input()
print(filter(accountType))

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