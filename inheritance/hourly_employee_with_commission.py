from hourly_employee import HourlyEmployee


class HourlyEmployeeWithCommission(HourlyEmployee):
    """Hourly pay plus a commission per closed sales contract."""

    def __init__(self, employee_id: int, name: str,
                 hours_worked: float, hourly_rate: float,
                 contracts_closed: int, commission_per_contract: float):
        super().__init__(employee_id, name, hours_worked, hourly_rate)
        self._contracts_closed = contracts_closed
        self._commission_per_contract = commission_per_contract

    def compute_pay(self) -> float:
        commission = self._contracts_closed * self._commission_per_contract
        return super().compute_pay() + commission
