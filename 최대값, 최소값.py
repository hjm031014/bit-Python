a=0
b=0
c=0
max=0
min=0

a=int(input("첫 번째 값을 입력하시오 : "))
b=int(input("두 번째 값을 입력하시오 : "))
c=int(input("세 번째 값을 입력하시오 : "))

if(a > b):
    if(a > c):
        max = a

        if(b > c):
            min = c
        else:
            min = b
    else:
        max = c
        min = b

else:
    if(b > c):
        max = b

        if(a > c):
            min = c
        else:
            min = a

    else:
        max = c
        min = a

print("세 수 중 최대값은",max,"이고, 최소값은",min,"입니다.")
          
