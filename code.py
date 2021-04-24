import io


n=int(input("Enter the number of employees:"))
a={}
f1=open("input.txt",'r')
for line in f1:
    line=line.strip()
    key,val=line.split(": ")
    a[key]=int(val)
print(a)
l=sorted(a.items(),key=lambda x:x[1])
print(l)
min=l[len(a)-1][1]
index=-1
for i in range(0,len(a)-n+1):
    v=l[i+n-1][1]-l[i][1]
    if v<min:
        min=v
        index=i
f2=open("output.txt",'w')
for i in range(index,index+n):
    val=l[i][1]
    v=str(val)
    s=l[i][0]+": "+v+'\n\n'
    f2.write(s)
f2.close()
f1.close()