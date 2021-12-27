#if 조건문
money1 = True
if money1: #조건문 뒤에 콜론(:) 기억
    print("택시를")
    print("타고")
    print("가라") #들여쓰기 맞추지 않으면 실행 오류 주의

money = 2000
if money>=3000:
    print("택시를 타라")
else:
    print("택시를 타지 마라.")

card = True
if money >=3000 or card : #and, or, not
    print("택시를 타라")
else:
    print("택시를 타지 마라.")

pocket = ['money', 'cellphone', 'paper', 'hat'] #리스트
if 'money' in pocket : #x in s
    print("택시를 타고 가라")
else:
    print("택시를 타지 마라.")

pocket = ['money', 'cellphone', 'paper', 'hat'] 
if 'money' in pocket :
    pass #조건문을 아무 것도 없이 실행(결과값 x)
else:
    print("카드를 꺼내라")
print('\n')

#주머니에 돈이 있으면 택시를 타고, 주머니에 돈이 없지만 카드가 있으면 택시를 타고, 
#돈도 없고 카드도 없으면 걸어가라.
pocket = ['cellphone', 'paper', 'hat']
card = False
if 'money' in pocket:
    print("택시를 타라")
else:
    if card:
        print("택시를 타라")
    else:
        print("걸어가라")

pocket = ['cellphone', 'paper', 'hat']
card = False
if 'money' in pocket:
    print("택시를 타라")
elif card: #같은 문장 elif문
        print("택시를 타라")
else:
    print("걸어가라")
print('\n')

#while
treehit = 0
while treehit <10:
    treehit = treehit + 1
    print("나무를 %d번 찍었습니다" %treehit)
    if treehit ==10:
        print("나무 넘어갑니다.")

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개 입니다" %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break #while문 빠져나가기
"""
coffee = 10
while True:
    money = int(input("돈을 넣어주세요: ")) #int(input()): 사용자에게 값을 입력받는 부분
    if money ==300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." %(money-300))
        coffee = coffee-1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." %coffee)
    if coffee ==0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
    print('\n')
"""
a= 0
while a<10:
    a = a+1
    if a %2 ==0: continue #while문을 빠져나가지 않고 while문 맨 처음(조건문)으로 돌아가게 함.
    print(a)

#for
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i) 

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

marks = [96, 60, 54, 80, 32]
number = 0
for mark in marks:
    number = number +1
    if mark >=60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)

marks = [96, 60, 54, 80, 32]
for mark in marks:
    number = number+1
    if mark < 60: continue
    print("%d번 학생은 축하합니다. 합격입니다" %number)
print("\n")

a = range(10) #숫자 리스트를 자동으로 만들어줌 (range 함수)
print(a) #(0,10)

add = 0
for i in range(1,11):
    add = add+i
    print(add)

for i in range(2,10): #구구단 출력
    for j in range(1,10):
        print(i*j, end= " ") #end: 해당 결과값을 그 줄에 계속 출력하려고 넣어줌
    print('') #다음줄부터 출력하게 해줌.

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)

result = [num*3 for num in a] #리스트 내포
print(result)