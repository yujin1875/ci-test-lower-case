from string_utils import reverse_string

def test_reverse_normal_string():
    """일반 문자열 뒤집기 테스트"""
    result = reverse_string("hello")
    assert result == "olleh"


def test_reverse_empty_string():
    """빈 문자열 테스트 - 빈 문자열은 그대로 반환"""
    result = reverse_string("")
    assert result == ""


def test_reverse_single_character():
    """한 글자 테스트 - 한 글자는 그대로 반환"""
    result = reverse_string("a")
    assert result == "a"


def test_reverse_palindrome():
    """회문 테스트 - 뒤집어도 같은 문자열"""
    result = reverse_string("level")
    assert result == "level"


def test_reverse_string_with_spaces():
    """공백 포함 문자열 테스트"""
    result = reverse_string("hello world")
    assert result == "dlrow olleh"
