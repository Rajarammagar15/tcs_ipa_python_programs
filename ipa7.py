n=int(input())
valid=0
invalid=0
for i in range(n):
    st=input()
    if all(chr.isalpha() or chr.isspace() for chr in st):
        valid+=1
    else:
        invalid+=1
print(valid)
print(invalid)