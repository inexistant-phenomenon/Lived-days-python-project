import time
d=[31,28,31,30,31,30,31,31,30,31,30,31]
bm=int(input("input birth-month : "))
while (bm<1) or (bm>12):
    bm=int(input("please input a valid month : "))
by=int(input("input birth-year : "))
while (by<1900) or (by>time.gmtime()[0]):
    by=int(input("please input a vlaid birth-year : "))
bd=int(input("input birthday : "))
while (bd<1) or (bd>d[bm-1]):
    bd=int(input("please input a valid day : "))
k=0
if by%4==0:
    k=d[1]+1
days=0
cy=time.gmtime()[0]
cm=time.gmtime()[1]
cd=time.gmtime()[2]
for j in range (by+1,cy):
    days+=365
    if j%4==0:
        days+=1
for i in range (0,cm-1):
    days+=d[i]
    if cy%4==0:
        days+=1
    days
days+=cd
days
for i in range(bm-1,11):
    if by%4==0:
        d[1]=29
    days+=d[i]
print(days+d[bm-1]-bd+1)
