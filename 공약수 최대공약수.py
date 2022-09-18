a=0 #첫 번째 값
b=0 #두 번째 값 
i=2 

a=int(input("숫자를 입력하시오 : "))
b=int(input("숫자를 입력하시오 : "))



while(1):
    if(a%i==0 and b%i==0):
        print("최대공약수 :",i)
        break
        
    else:
        i+=1


i=0

while(1):
    i+=1
    if(a%i==0 and b%i==0):
        print("공약수 :",i)
        


'''
----------------------------------
print("공약수 :", end="")

    while(a>i):
    if(a%i==0 and b%i==0):
        print(i, end=" ")
        
    i+=1
-----------------------------------
'''

# P.127, 공약수와 최대공약수     

