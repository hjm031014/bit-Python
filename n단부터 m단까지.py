a=0
b=0
c=1

a=int(input("첫 번째 수를 입력하시오. : "))
b=int(input("두 번째 수를 입력하시오. : "))



if(a>b):
    num=a
    a=b
    b=num

if(b>=10 or a<2):
    print("2~9 사이의 숫자를 입력하시오.")
else:

    while(a<b+1):
        while(c<10):
            print(a, "*" , c , "=" , a*c)
            c+=1
        c=1
        a+=1
