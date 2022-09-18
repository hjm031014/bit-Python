a=0
b=1
'''
while(a<=5):
    while(b<a):
        print("0 ",end="")
        b+=1
    a+=1
    print("*")
    b=1
'''

while(a < 5):
    print("0" * a + "*")
    a = a + 1
