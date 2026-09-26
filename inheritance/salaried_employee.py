from employee import Employee


class SalariedEmployee(Employee):
    """Paid a fixed monthly salary."""

    def __init__(self, employee_id: int, name: str, monthly_salary: float):
        super().__init__(employee_id, name)
        self._monthly_salary = monthly_salary

    def compute_pay(self) -> float:
        return self._monthly_salary
