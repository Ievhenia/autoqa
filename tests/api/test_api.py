import pytest


class User:

    def __init__(self) -> None:
        self.name = 'Ievhenia'
        self.second_name = 'Prydatkevych'


@pytest.fixture
def user():
    yield User()

def test_remove_name(user):
    user.name = ''
    assert user.name == ''

def test_name(user):
    assert user.name == 'Ievhenia'

def test_second_name(user):
    assert user.second_name == 'Prydatkevych'
