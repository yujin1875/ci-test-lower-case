# [구구단 과제 3] 반복 실행되는 구구단 (메뉴형)

while True:
    dan = int(input("몇 단을 출력할까요? "))
    start = int(input("시작 숫자를 입력하세요: "))
    end = int(input("끝 숫자를 입력하세요: "))

    for i in range(start, end + 1):
        print(dan, "x", i, "=", dan * i)

    cont = input("계속하시겠습니까? (yes/no): ")

    if cont.lower() == "no":   # no 입력 → 종료
        print("프로그램을 종료합니다.")
        break
    # yes → while 계속
