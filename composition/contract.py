from abc import ABC, abstractmethod


class Contract(ABC):
    """Abstraction for HOW an employee is paid (their base pay)."""

    @abstractmethod
    def compute_pay(self) -> float:
        ...
