from commission import Commission


class ContractCommission(Commission):
    """Commission per closed sales contract: contracts_closed * commission_per_contract."""

    def __init__(self, contracts_closed: int, commission_per_contract: float):
        self._contracts_closed = contracts_closed
        self._commission_per_contract = commission_per_contract

    def compute_commission(self) -> float:
        return self._contracts_closed * self._commission_per_contract
