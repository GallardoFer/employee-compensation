from salaried_employee import SalariedEmployee


class SalariedEmployeeWithCommission(SalariedEmployee):
    """Monthly salary plus a commission per closed sales contract."""

    def __init__(self, employee_id: int, name: str, monthly_salary: float,
                 contracts_closed: int, commission_per_contract: float):
        super().__init__(employee_id, name, monthly_salary)
        self._contracts_closed = contracts_closed
        self._commission_per_contract = commission_per_contract

    def compute_pay(self) -> float:
        commission = self._contracts_closed * self._commission_per_contract
        return super().compute_pay() + commission
