import pytest

# ========== 테스트 대상 ==========
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b


# ========== Fixture 정의 ==========
@pytest.fixture
def calculator():
    """Calculator 객체를 미리 만들어둡니다"""
    print("Calculator 생성!")  # 언제 만들어지는지 확인용
    return Calculator()


# ========== 테스트 ==========
def test_더하기(calculator):
    result = calculator.add(2, 3)
    assert result == 5

def test_빼기(calculator):
    result = calculator.subtract(5, 3)
    assert result == 2

def test_일반():
    # fixture를 안 쓰는 테스트도 가능
    assert 1 + 1 == 2
