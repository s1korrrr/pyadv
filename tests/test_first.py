from types import ModuleType


def test_1():
    import shekels

    assert type(shekels) == ModuleType


def test_2():
    assert True == True
