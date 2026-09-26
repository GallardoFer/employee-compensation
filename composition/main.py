from employee import Employee
from hourly_contract import HourlyContract
from salaried_contract import SalariedContract
from freelancer_contract import FreelancerContract
from contract_commission import ContractCommission


def main():
    # Composition root: this is the ONE place that decides which pieces go together
    employees = [
        Employee(1, "Ana Lopez", HourlyContract(hours_worked=160, hourly_rate=120)),
        Employee(2, "Bruno Diaz", SalariedContract(monthly_salary=25000)),
        Employee(3, "Carla Ruiz", FreelancerContract(projects_delivered=3, fee_per_project=8000)),
        Employee(4, "Diego Mora",
                 HourlyContract(hours_worked=100, hourly_rate=110),
                 ContractCommission(contracts_closed=4, commission_per_contract=1500)),
        Employee(5, "Elena Soto",
                 SalariedContract(monthly_salary=22000),
                 ContractCommission(contracts_closed=6, commission_per_contract=1200)),
        Employee(6, "Fer Nava",
                 FreelancerContract(projects_delivered=2, fee_per_project=9000),
                 ContractCommission(contracts_closed=3, commission_per_contract=2000)),
    ]

    print("Payroll (composition version)")
    for employee in employees:
        print(f"{employee.employee_id:>3}  {employee.name:<12} ${employee.compute_pay():>10,.2f}")


if __name__ == "__main__":
    main()
