#리스트 자료형
a = [1,2,3,[1,2]] #리스트 생성, 사용
b = ['life', 'is']
print(a)
print(b)
print(a[0]) ##1
print(a[0]+a[1]) ##1+2=3
print(a[-1]) ##마지막 요소 가리킴 / 문자열이랑 동일
print('\n')

print(a[-1][0]) ##마지막 요소 리스트에서 요소 불러냄
print(a[-1][1])

c = [1, 2, ['a', 'b', ['life', 'is']]] #삼중 구조 리스트
print(c[2][2][0]) #삼중 구조 리스트 출력

d = [1,2,3,4,5]
print(d[0:2]) #슬라이싱(나눈다) / 문자열에서 하는 것과 동일
print(d[:2]) ##a[2]까지 출력
print(d[:]) ## 전체 출력
print('\n')

e = [1,2,3]
f = [4,5,6]
print(e+f) #리스트 연산(더하기)
print(e*3) #리스트 연산(곱하기)
print(len(e)) #리스트 길이 구하기(len)
print(str(a[2])+"hi") #str함수 = 정수나 실수를 문자열의 형태로 바꿔줌
print('\n')

e[2] = 10 #리스트 값 수정
print(e)
del e[1] #삭제 함수 // 리스트 요소 삭제
print(e)
del f[0:2] 
print(f)
print('\n')

e.append(4) #리스트에 요소 추가(맨 마지막에 ()안에 있는 것 추가)
print(e)

e.sort() #리스트 정렬 (순서대로 정렬해줌)
print(e)

e.reverse() #리스트 뒤집기(현재의 리스트를 거꾸로 뒤집기)
print(e)

print(e.index(10)) #위치 반환(index(x)/ 리스트에 x 값이 있으면 위치 값을 돌려줌)
print('\n')

e.insert(0, 20) #리스트에 요소 삽입(0번째 위치에 20삽입)
print(e)

g = [1,2,3,1,2,3]
g.remove(3) #리스트 요소 제거(첫 번째로 나오는 x 제거 / 한 번만)
print(g)

e.pop() #리스트 요소 끄집어 내기(맨 마지막 요소 돌려주고 그 요소 삭제)
print(e)

print(g.count(1)) #리스트에 포함된 요소 x의 갯수 세기

e.extend([6,5]) #리스트 확장 / x에는 리스트만 올 수 있음
print(e)

#튜플 자료형
t1 = (1,2,'a','b') #튜플
print(t1[0]) #튜플 인덱싱
print(t1[1:]) #튜플 슬라이싱

t2=(3,4)
print(t1+t2) #튜플 더하기
print(t2*3) #튜플 곱하기
print(len(t2)) #튜플 길이 구하기(len)
print('\n')

#딕셔너리 자료형
dic = {'name': 'seoyeon', 'phone': '01011112233', 'birth': '0831'}
print(dic)

a = {1:'a'}
a[2] = 'b' #딕셔너리 쌍 추가
print(a)
del a[1] #딕셔너리 요소 삭제
print(a)
print(dic['name']) #딕셔너리에서 key 사용해 value 얻기
print(a[2])

print(dic.keys()) #key 리스트 만들기(keys) / 딕셔너리의 key들만 모아서 객체 돌려줌.

print(list(dic.keys())) #key 객체 리스트로 변화

print(dic.values()) #value 리스트 만들기

print(dic.items()) #key,value 쌍 얻기(items)

print(dic.get('name')) #key로 value 얻기(get)
print(dic.get('birth'))

print('name' in dic) #key가 딕셔너리 안에 있는지 조사(in)
print('email' in dic)

print(dic.clear()) #value 쌍 모두 지우기(clear)