num=0

num=int(input("출력 개수 : "))

count=0
c=0
max=2
n=0

while(c<num):
    for n in range(1,max+1,1):
        if(max%n==0):
            count+=1
    if(count==2):
        print(max,end=" ")
        c+=1
    max+=1
    count=0
