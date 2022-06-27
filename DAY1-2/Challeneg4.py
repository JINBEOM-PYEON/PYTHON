#문제 1 : 정수(1 ~ 100) 1개를 입력 받아 1부터 그 수까지 짝수의 합을 출력하시오.
#• for, while 문 선택
#• 문제 2 : 영문 소문자 q가 입력될 까지 입력 문자를 무한 출력하시오.
#• While 문과 if문 활용
num = int(input("정수 1개를 입력하세요: "))
cnt = 0

if num <= 100:
    for i in range(1, num+1):
        if i % 2 == 0:
            cnt += i
print(num, "까지 짝수의 합: ", cnt)




# 문제 2 : 영문 소문자 q가 입력될 까지 입력 문자를 무한 출력하시오.
# While 문과 if문 활용

while True:
    val = input("q가 입력될 때 까지 무한 반복: ")
    if val == 'q':
        break
    else:
        print("입려 문자: ", val)