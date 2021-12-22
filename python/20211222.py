#집합 자료형
s1 = set([1,2,3])
print(s1)
s2 = set("Hello") #중복 허용X, 순서x > 인덱싱x
print(s2)
print('\n')

s3 = set([1,2,3,4,5,6])
s4 = set([4,5,6,7,8,9])
print(s3 & s4) #교집합
print(s3.intersection(s4)) #교집합
print(s3|s4) #합집합
print(s3.union(s4)) #합집합
print(s3-s4) #차집합
print(s3.difference(s4)) #차집합

s3.add(7) #값 1개 추가하기(add)
print(s3)
s3.update([8,9,10]) #값 여러개 추가하기(update)
print(s3)
s3.remove(7) #값 제거하기(remove) - 1개씩 지울 수 있음
print(s3)
print('\n')

#불 자료형
a = True
b = False
print(1==1) #조건문의 결과로 t,f 돌려줌.
print(2<1)

print(bool('python')) #불 연산
print(bool(''))

print(bool([1,2,3]))
print(bool([]))
print('\n')

#변수
a = [1,2,3]
b = a
print(id(a)) #메모리 주소 출력(id)
print(id(a))
print(a is b) #동일한 객체를 가리키고 있는지 판단(is)

a[1] = 4
print(a) #a[1]만 바꿨지만 a,b 둘다 같은 리스트를 가리키고 있어서 둘 다 바뀜.
print(b)

c = [4,5,6]
d = c[:]
print(d)

e,f = 'python', 'life' #튜플로 변수 만들기
print(e)