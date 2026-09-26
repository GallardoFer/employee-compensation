from contract import Contract


class FreelancerContract(Contract):
    """Paid per delivered project: projects_delivered * fee_per_project."""

    def __init__(self, projects_delivered: int, fee_per_project: float):
        self._projects_delivered = projects_delivered
        self._fee_per_project = fee_per_project

    def compute_pay(self) -> float:
        return self._projects_delivered * self._fee_per_project
