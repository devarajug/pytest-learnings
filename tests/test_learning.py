import pytest

@pytest.mark.tag("functional")
def test_sample():
    assert True

@pytest.mark.tag("e2e")
def test_sample_1():
    assert True