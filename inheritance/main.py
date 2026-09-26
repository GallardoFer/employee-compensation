from hourly_employee import HourlyEmployee
from salaried_employee import SalariedEmployee
from freelancer import Freelancer
from hourly_employee_with_commission import HourlyEmployeeWithCommission
from salaried_employee_with_commission import SalariedEmployeeWithCommission
from freelancer_with_commission import FreelancerWithCommission


def main():
    employees = [
        HourlyEmployee(1, "Ana Lopez", hours_worked=160, hourly_rate=120),
        SalariedEmployee(2, "Bruno Diaz", monthly_salary=25000),
        Freelancer(3, "Carla Ruiz", projects_delivered=3, fee_per_project=8000),
        HourlyEmployeeWithCommission(4, "Diego Mora", hours_worked=100, hourly_rate=110,
                                     contracts_closed=4, commission_per_contract=1500),
        SalariedEmployeeWithCommission(5, "Elena Soto", monthly_salary=22000,
                                       contracts_closed=6, commission_per_contract=1200),
        FreelancerWithCommission(6, "Fer Nava", projects_delivered=2, fee_per_project=9000,
                                 contracts_closed=3, commission_per_contract=2000),
    ]

    print("Payroll (inheritance version)")
    for employee in employees:
        # Polymorphism: same call, each class computes pay its own way
        print(f"{employee.employee_id:>3}  {employee.name:<12} ${employee.compute_pay():>10,.2f}")


if __name__ == "__main__":
    main()
