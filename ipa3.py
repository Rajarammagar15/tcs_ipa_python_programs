st = input()
st1 = ''
n = int(input())
temp = n + (len(st)//2)
if temp < len(st):
    for char in st[len(st)//2 : temp]:
        st1 += char
else:
    for char in st[len(st)//2 : len(st)]:
        st1 += char
print(st1)
