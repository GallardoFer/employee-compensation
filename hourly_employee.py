from employee import Employee


class HourlyEmployee(Employee):
    """Paid by the hour: hours_worked * hourly_rate."""

    def __init__(self, employee_id: int, name: str,
                 hours_worked: float, hourly_rate: float):
        super().__init__(employee_id, name)
        self._hours_worked = hours_worked
        self._hourly_rate = hourly_rate

    def compute_pay(self) -> float:
        return self._hours_worked * self._hourly_rate
