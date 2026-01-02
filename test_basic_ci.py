# --------------------------------------------
# 이 테스트는 CI(GitHub Actions)가
# push 될 때마다 정상 동작하는지 확인하기 위한
# "연습용 테스트"입니다.
# --------------------------------------------

def test_ci_is_working():
    """
    이 테스트가 통과하면:
    - pytest가 정상 설치됨
    - GitHub Actions에서 테스트가 실행됨
    - CI 파이프라인이 살아있음
    """
    assert 1 + 1 == 2

def test_ci_should_fail():
    assert 1 + 1 == 3
