
a=0 #과목 수
j=0 #점수 
n=0 #누적
sum=0 #총 합점수

a=int(input("과목 수를 입력하시오. "))

while(n<a):
    j=int(input("점수를 입력하시오. "))
    sum+=j
    n+=1

sum=sum/a
print("평균은", sum,"점 입니다")


a=0 #과목 수
j=0 #점수 
n=0 #누적
sum=0 #총 합점수

a=int(input("과목 수를 입력하시오. "))

for n in range(0,a,1):
    j=int(input("점수를 입력하시오. "))
    sum+=j

sum=sum/a
print("평균은", sum,"점 입니다")
