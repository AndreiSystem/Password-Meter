from abc import ABC

from app.requirement.requirement import Requirement


class Rate(ABC):
    def __init__(self, weight: int):
        self._weight = weight

    def calculate(self, requirement: Requirement) -> int:
        return len(requirement.get_value()) * self._weight




