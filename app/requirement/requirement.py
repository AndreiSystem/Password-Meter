from abc import ABC

from app.password.password import Password
from app.rate.rate import Rate


class Requirement(ABC):
    def __init__(self, password: Password, rate: Rate):
        self._password = password
        self._rate = rate

    def get_value(self):
        return self._password.get_value()

    def get_count(self) -> int:
        pass

    def get_bonus(self) -> int:
        pass