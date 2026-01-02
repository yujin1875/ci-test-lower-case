# 2. 조건문
#
# age 변수에 17이라는 값을 저장한다.
age = 17

# if문: "만약 age가 18 이상이면" 을 검사한다.
# age >= 18 의 결과가 참(True)이면 들여쓴 코드를 실행한다.
if age >= 18:
    print("성인입니다.")  # 조건이 참일 때 실행됨
else:
    # if 조건이 거짓(False)일 때 대신 실행된다.
    print("미성년자입니다.")

# score 변수에 85를 저장한다.
score = 85

# if ~ elif ~ else 구조
# 위에서부터 순서대로 조건을 검사하면서
# 가장 먼저 True가 되는 조건의 코드만 실행한다.
if score >= 90:
    print("A 학점")
elif score >= 80:
    print("B 학점")
elif score >= 70:
    print("C 학점")
else:
    print("F 학점")

############################################

a = 10
b = 20

# == : 같다
print("a == b :", a == b)      # 10 == 20 → False

# != : 같지 않다
print("a != b :", a != b)      # 10 != 20 → True

# > : 크다
print("a > b  :", a > b)       # 10 > 20 → False

# < : 작다
print("a < b  :", a < b)       # 10 < 20 → True

# >= : 크거나 같다
print("a >= b :", a >= b)      # 10 >= 20 → False

# <= : 작거나 같다
print("a <= b :", a <= b)      # 10 <= 20 → True

print("---------------------------")

# 문자열 비교도 가능
x = "apple"
y = "banana"

print("x == y :", x == y)      # 문자열이 같은지
print("x != y :", x != y)      # 문자열이 다른지
print("x < y  :", x < y)       # 사전 순 비교 → True ('a' < 'b')
print("x > y  :", x > y)       # False
