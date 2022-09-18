sum=int(input("입력 : "))

for a in range(500,sum+1,500): #빵의 개수
    for b in range(700,sum+1,700): #과자의 개수
        for c in range(400,sum+1,400): #콜라의 개
            if(a+b+c==sum):
                print("빵",a//500,"과자",b//700,"음료수",c//400)
        
