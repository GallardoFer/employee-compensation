from abc import ABC, abstractmethod


class Employee(ABC):
    """Base class: every employee has an id, a name and a way to be paid."""

    def __init__(self, employee_id: int, name: str):
        self.employee_id = employee_id
        self.name = name

    @abstractmethod
    def compute_pay(self) -> float:
        """Each subclass decides how the employee is paid."""