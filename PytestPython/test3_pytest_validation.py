import pytest

@pytest.fixture(scope="module")
def prework():
    print("\n[setup module]")
    return "pass"

@pytest.fixture(scope="function")
def second_work():
    print("\n[setup function]")
    yield
    print("\n[teardown function]")
@pytest.mark.smoke
def test_initial_check(prework, second_work):
    print("This is First Check")
    assert prework == "pass"

def test_second_check(prework, second_work):  # <-- use the same fixture names
    print("This is Second Check")
    assert prework == "pass"                   # <-- prework is in scope now
