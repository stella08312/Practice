#문자열 출력
print("=" * 50)
print("My Program")
print("=" * 50)

#문자열 인덱싱 활용
a = "life is too short, you need python"
b = a[0]+a[1]+a[2]+a[3]
print(b)

#문자열 포매팅
print("I eat %d apples." %3) 

#포맷코드와 숫자 함께 사용
print("%10s" %"hi")
print("%0.4f" %3.4125456)

#format 함수를 사용한 포매팅
print("I eat {0} apples" .format(3))
print("I eat {0} apples" .format("five"))
print("{0:>10}" .format("hi"))
print("{0:^10}" .format("hi")) 

#f 문자열 포매팅
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

#문자 개수 세기(cout) 
a = "hobby"
print(a.count('b')) #문자열 중 문자 b의 갯수 알려줌

#위치 알려주기(find)
a = "python is the best choice"
print(a.find('t'))

#위치 알려주기2(index)
a = "life is too short"
print(a.index('t'))

#문자열 삽입(join)
print(",".join('abcd'))

#소문자를 대문자로 바꾸기(upper)
a = "hi"
print(a.upper())

#대문자를 소문자로 바꾸기(lower)
a = "HI"
print(a.lower())

#왼쪽 공백 지우기(lstrip)
a = " hi "
print(a.lstrip())

#오른쪽 공백 지우기(rstrip)
a = " hi "
print(a.rstrip())

#양쪽 공백 지우기(strip)
a = " hi "
print(a.strip())

#문자열 바꾸기(replace)
a = "life is too short"
print(a.replace("life", "your leg"))

#문자열 나누기(split)
a = "life is too short"
print(a.split())
print(a.split(':'))