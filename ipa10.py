def target(st,n):
    s=''
    t=len(st)//2
    if t+n<=len(st):
        for i in range(t,t+n):
            s+=st[i]
    else:
        for i in range(t,len(st)):
            s+=st[i]
    return s

st=input()
n=int(input())
print(target(st,n))
