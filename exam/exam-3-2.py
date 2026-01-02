# [구구단 과제 2] 사용자 입력 기반 1회 실행 구구단

dan = int(input("몇 단을 출력할까요? "))
start = int(input("시작 숫자를 입력하세요: "))
end = int(input("끝 숫자를 입력하세요: "))

for i in range(start, end + 1):
    print(dan, "x", i, "=", dan * i)
