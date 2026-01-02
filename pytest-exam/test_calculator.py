# 1) 테스트할 대상 Import
import pytest
from calculator import Calculator

# ===============================================================
# pytest의 기본 규칙
# ---------------------------------------------------------------
# - 테스트 함수 이름은 반드시 test로 시작해야 한다.
# - assert 문을 사용하여 기대값과 실제값을 비교한다.
# - 클래스 안에 테스트를 넣을 수도 있지만, 메서드 이름도 test로 시작해야 한다.
# ===============================================================

@pytest.fixture
def calc():
    """테스트 전에 불리는 '준비 코드'"""
    return Calculator()

def test_add():
    """
    테스트 케이스 1: add 메서드가 정상적으로 두 수를 더하는지 테스트한다.
    """
    calc = Calculator()       # 테스트할 객체 생성
    result = calc.add(2, 3)   # 실행
    assert result == 5        # 기대값과 비교 (pass / fail 결정)


def test_subtract():
    """
    테스트 케이스 2: subtract 메서드가 두 수를 올바르게 빼는지 테스트한다.
    """
    calc = Calculator()
    result = calc.subtract(10, 4)
    assert result == 6
