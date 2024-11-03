# import
import random

# 초기
print("비밀번호 생성 프로그램 \n") 

# 가능한 글자
words = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+-=,./<>?:";\|~`[}]{1234567890'

# 입력
number = int(input("생성되는 비밀번호의 수 : "))
length = int(input("비밀번호의 길이 : "))

# 출력
print("생성된 비밀번호는 아래와 같습니다. :")

# 생성 및 비밀번호 출력
for pwd in range(number) : # 생선되는 비밀번호의 수 만큼 반복
    password = '' # 비밀번호가 담기는 변수
    for i in range(length) : # 비밀번호의 길이 만큼 반복
        password += random.choice(words) # words에 있는 글자 중 무작위로 선택하여 password에 저장
    print(password) # 생성된 비밀번호를 출력