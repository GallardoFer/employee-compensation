from contract import Contract


class SalariedContract(Contract):
    """Paid a fixed monthly salary."""

    def __init__(self, monthly_salary: float):
        self._monthly_salary = monthly_salary

    def compute_pay(self) -> float:
        return self._monthly_salary
