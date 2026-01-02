import pytest


class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []
    
    def add_score(self, score):
        self.scores.append(score)
    
    def average(self):
        if len(self.scores) == 0:
            return 0
        total = sum(self.scores)
        return total / len(self.scores)

#############################################

@pytest.fixture
def student():
    return Student("철수")


def test_학생_이름(student):
    assert student.name == "철수"


def test_점수_추가(student):
    student.add_score(80)
    assert 80 in student.scores


def test_평균_계산(student):
    student.add_score(80)
    student.add_score(90)
    student.add_score(100)
    assert student.average() == 90
