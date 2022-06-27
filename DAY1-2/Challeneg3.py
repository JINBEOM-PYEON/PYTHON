#• 문제 : 정수 3개 입력 받아 합과 평균 출력하시오.
# map(int, input().split()) 활용, 또는 3개 정수 캐스팅
a, b, c = map(int,input('정수를 3개 입력 : ').split())
a=int(a)
b=int(b)
c=int(c)
print(a+b+c/3)