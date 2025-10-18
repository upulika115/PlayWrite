import pytest

@pytest.fixture(scope="module")
def preSetupWork():
    print("I setup browser instance")