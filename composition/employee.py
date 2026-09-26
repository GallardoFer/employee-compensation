from contract import Contract
from commission import Commission


class Employee:
    """An employee HAS-A Contract and MAY-HAVE-A Commission."""

    def __init__(self, employee_id: int, name: str,
                 contract: Contract, commission: Commission | None = None):
        self.employee_id = employee_id
        self.name = name
        self._contract = contract        # required collaborator (1)
        self._commission = commission    # optional collaborator (0..1)

    def compute_pay(self) -> float:
        pay = self._contract.compute_pay()
        if self._commission is not None:
            pay += self._commission.compute_commission()
        return pay
