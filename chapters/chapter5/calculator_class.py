class Calculator:
    def __init__(self):
        print("생성자 작동~")
        # __init__은 "생성자"
        # 객체가 만들어질 때 자동으로 딱 한 번 실행됨

        self.result = 0
        # self.result는 이 객체가 계속 들고 다닐 값(상태)
        # 객체 안에 result라는 변수를 만들어 둠


    def add(self, x):
        # 메서드(method)
        # self는 "이 메서드를 호출한 객체 자신"을 의미함
        # 파이썬이 자동으로 self를 넘겨줌 (우리가 직접 안 넣음)

        self.result += x
        # 객체가 들고 있는 result 값을 누적해서 변경

        return self.result
        # 변경된 결과를 반환


    def sub(self, x):
        self.result -= x
        return self.result


# ===============================
# 객체 생성
# ===============================

# Calculator는 설계도(클래스)
# calc는 실제 계산기 하나(객체, 인스턴스)
calc = Calculator()

# ===============================
# 메서드 호출
# ===============================

print(calc.add(10))  # 10
# result = 0 + 10 → 10

print(calc.sub(3))   # 7
# result = 10 - 3 → 7

print(calc.add(5))   # 12
# result = 7 + 5 → 12

##############################
# 
# 함수 방식과 가장 큰 차이:
# 함수: 계산만 하고 끝
# 클래스: 값을 저장하면서 계속 사용 가능
##############################
# 함수지향때와 달리 객체지향(OOP) 패턴을 쓰면
# result라는 값을(self.result → 객체가 상태를 기억함)
# 특정 객체(Calculator라는 클래스의 객체, 위에서는 calc라는 변수에 저장되어 있다)
# 에 저장해두고 활용할 수 있다.
##############################