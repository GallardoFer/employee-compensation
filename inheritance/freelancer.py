from employee import Employee


class Freelancer(Employee):
    """Paid per delivered project: projects_delivered * fee_per_project."""

    def __init__(self, employee_id: int, name: str,
                 projects_delivered: int, fee_per_project: float):
        super().__init__(employee_id, name)
        self._projects_delivered = projects_delivered
        self._fee_per_project = fee_per_project

    def compute_pay(self) -> float:
        return self._projects_delivered * self._fee_per_project
