def searchstr(l,st):
    for s in l:
        if s==st:
            return l.index(s)


n=int(input())
l=[]
for i in range(n):
    l.append(input())
st=input()
print(searchstr(l,st))