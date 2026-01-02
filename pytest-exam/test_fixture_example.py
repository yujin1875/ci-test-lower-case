import pytest

@pytest.fixture
def sample_data():
    print("\n💿 sample_data 준비됨!")  # 언제 실행되는지 보기 위한 로그
    return {"message": "hello", "count": 1}


# ============================================================
# 🧩 scope="module"
# ------------------------------------------------------------
# fixture가 얼마나 오래 유지될지 결정하는 옵션.
#
# 기본값(scope="function")  → 테스트 함수 1개 실행마다 새로 만든다.
# scope="module" → 이 파일(test_fixture_example.py) 전체에서 딱 1번만 만든다.
# ============================================================
@pytest.fixture(scope="module")
def config():
    print("\n☑️config() 실행됨! (module 스코프: 파일 전체에서 1번만 생성)")
    return {"timeout": 30}


# ============================================================
# 🧩 yield를 이용한 setup → teardown 자동 처리
# ------------------------------------------------------------
# yield는 '중간에서 멈췄다가 다시 실행되는 return'이라고 보면 된다.
#
# yield f 위쪽 : 테스트 시작 전에 실행되는 setup 영역
# yield f 아래쪽 : 테스트 끝난 후 자동 실행되는 teardown 영역
#
# return은 teardown을 넣을 수 없기 때문에
# '정리 작업'이 필요한 fixture에서는 반드시 yield 사용.
# ============================================================

@pytest.fixture
def temp_file():
    print("\n📂 파일 생성 (setup)")
    f = open("test.txt", "w")

    # 테스트 실행 중 사용할 객체를 제공
    yield f

    # 테스트 끝나고 자동으로 실행됨
    print("🧹 파일 닫기 (teardown)")
    f.close()


# ============================================================
# 🧪 4. 실제 테스트들
# ------------------------------------------------------------
# sample_data, config, temp_file fixture를 실제로 이용하여 테스트.
# ============================================================


def test_sample_data_usage(sample_data):
    # sample_data는 fixture에서 return한 dict
    assert sample_data["message"] == "hello"
    sample_data["count"] += 1          # 테스트에서 값 수정 가능


def test_config_module_scope(config):
    # config는 파일 전체에서 1번만 생성된 객체
    assert config["timeout"] == 30


def test_file_write(temp_file):
    # temp_file fixture는 내부적으로 yield f 로 f가 전달됨
    temp_file.write("pytest fixture with yield!")
    assert True


def test_second_file_write(temp_file):
    # temp_file은 function 스코프이므로 매 테스트마다 새로 생성됨
    temp_file.write("another test writing!")
    assert True


# 👉🏻pytest 파일명 -s 로 실행해서 실제 print되는 모습을 보자
# ============================================================
# 📌 이 파일의 실행 흐름
# ------------------------------------------------------------
# 1) pytest가 test_ 로 시작하는 함수를 찾음
# 2) test_sample_data_usage → sample_data() 먼저 실행됨 → 테스트 실행
# 3) test_config_module_scope → config() 실행됨 (딱 1번)
# 4) test_file_write → temp_file() setup → 테스트 → teardown
# 5) test_second_file_write → temp_file() setup → 테스트 → teardown
# ============================================================
