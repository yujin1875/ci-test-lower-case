import pytest

# ============================================================
# ✨ 1) 단일 매개변수 parametrize 예시
# ============================================================
@pytest.mark.parametrize("number", [1, 2, 3])
def test_is_positive(number):
    """
    이 테스트는 3번 실행된다:

    1) number = 1
    2) number = 2
    3) number = 3

    pytest가 알아서 number에 값들을 넣어서 반복 실행해준다.
    """
    assert number > 0



# ============================================================
# ✨ 2) 여러 매개변수(tuple) 사용 예시
# ============================================================
def add(a, b):
    """단순 더하기 함수"""
    return a + b


@pytest.mark.parametrize(
    "a, b, expected",       # 테스트 함수 매개변수 이름 3개
    [
        (1, 2, 3),          # 첫 번째 테스트 케이스
        (10, 5, 15),        # 두 번째 테스트 케이스
        (-1, 1, 0),         # 세 번째 테스트 케이스
    ]
)
def test_add(a, b, expected):
    """
    이 테스트는 3번 실행된다.

    1) a=1, b=2, expected=3
    2) a=10, b=5, expected=15
    3) a=-1, b=1, expected=0

    각 테스트는 독립적으로 수행되는 "별도 테스트"처럼 동작한다.
    pytest 출력에서도 '3개 중 몇 개 성공' 형태로 표시됨.
    """
    # Act
    result = add(a, b)

    # Assert
    assert result == expected

 