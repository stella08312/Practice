#백준 10430
a,b,c = map(int, input().split())
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

#백준 2588
a = int(input())
b = int(input())
print(a*(b%10))
print(a*((b%100)//10))
print(a*(b//100))
print(a*b)

#백준 1330
a,b = map(int, input().split())    
if(a>b):
    print('>')
elif(a<b):
    print('<')
else:
    print('==')