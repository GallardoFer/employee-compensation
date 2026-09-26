from abc import ABC, abstractmethod


class Commission(ABC):
    """Abstraction for an OPTIONAL extra amount added on top of base pay."""

    @abstractmethod
    def compute_commission(self) -> float:
        ...
