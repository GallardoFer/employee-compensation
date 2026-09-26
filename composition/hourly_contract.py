from contract import Contract


class HourlyContract(Contract):
    """Paid by the hour: hours_worked * hourly_rate."""

    def __init__(self, hours_worked: float, hourly_rate: float):
        self._hours_worked = hours_worked
        self._hourly_rate = hourly_rate

    def compute_pay(self) -> float:
        return self._hours_worked * self._hourly_rate
