# [구구단 과제 1] 하드코딩된 구구단

# 2단을 고정으로 출력한다. (사용자 입력 없음)
dan = 2

for i in range(1, 10):
    print(dan, "x", i, "=", dan * i)
    cont = input("계속하시겠습니까? (yes/no): ")

    if cont.lower() == "no":   # no 입력 → 종료
        print("프로그램을 종료합니다.")
        break
    # yes → while 계속
