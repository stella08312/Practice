#함수
def add(a,b): #함수 선언
    return a+b
a = 3
b = 4
c = add(a,b) #a,b는 매개변수
print(c)
print(add(3,4)) #3,4는 인수

def say(): #입력값이 없는 함수
    return 'hi'
a = say()
print(a)

def add(a,b): #결과값이 없는 함수
    print("%d, %d의 합은 %d입니다." %(a,b,a+b))
add(3,4)

def say(): #입력값,결과값이 없는 함수
    print('hi')
say() #>>이렇게 하면 함수 사용 가능

def add(a,b): #매개변수 지정하여 함수 호출
    return a+b
result = add(a=3, b=7)
print(result)

def add_many(*args): #여러 개의 입력값을 받는 함수 / 매개 변수 앞에 * 붙이면 튜플로 만들어 줌.
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)
result = add_mul('mul', 1,2,3,4,5)
print(result)

def say_myself(name, old, man=False): #매개변수 초깃값 미리 설정
    print("나의 이름은 %s입니다." %name)
    print("나의 나이는 %d입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("오서연", 20)

a = 1
def vartest(a):
    a =a +1

vartest(a)
print(a)

add = lambda a, b:a+b #def와 동일한 역할 (주로 한 줄로 간결하게 만들 때)
result = add(3,4)
print(result)
print('\n')

#사용자 입력과 출력
#number = input("숫자를 입력하세요: ") #input: 입력되는 모든 것을 문자열로 취급
#print(number)

print("life", "is", "too", "short") # + 연산을 한 것처럼 출력

#파일 읽고 쓰기
f = open("새파일.txt", 'w')
for i in range(1,11):
    data = "%d번째 줄 입니다.\n" %i
    f.write(data) #data를 파일 객체 f에 써라
f.close()

f = open("새파일.txt", 'r')
line = f.readline() #파일 읽어드림
print(line)
f.close()

f = open("새파일.txt", 'r')
lines = f.readlines() #파일을 읽어 리스트로 돌려줌
for line in lines:
    print(line)
f.close()

f = open("새파일.txt", 'r')
data = f.read() #파일 전체를 문자열로 돌려줌
print(data)
f.close()