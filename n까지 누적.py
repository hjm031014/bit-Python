a=0 #입력
b=1 #증감
sum=0 #누적

a=int(input("첫번째 숫자 입력"))

while(b<=a):
    sum+=b
    b+=1
    
print("1부터",a,"까지의 누적합은",sum, "입니다")

