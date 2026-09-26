# Employee Compensation — Inheritance vs Composition

Homework for the Software Design course (Session 9: Interfaces, Dependencies & Composition).

The same employee-compensation problem is implemented twice to compare how each design
represents variation and dependencies.

> nota: los dos programas hacen lo mismo, solo cambia como estan organizados por dentro

| Folder | Content |
|---|---|
| `inheritance/` | Inheritance-based design (one class per file) |
| `composition/` | Composition-based design (one class per file) |
| `uml/` | UML class diagrams for both designs |

## Pay rules

| Type | Pay |
|---|---|
| Hourly | `hours_worked * hourly_rate` |
| Salaried | `monthly_salary` |
| Freelancer | `projects_delivered * fee_per_project` |
| Commission (optional) | adds `contracts_closed * commission_per_contract` |

> las formulas de pago no venian en las presentaciones, las definimos nosotros

`ContractCommission` means a commission per closed sales contract.
It is not related to the `Contract` classes that define the base pay.

> ojo: aqui "contract" significa contrato de venta, no el tipo de contrato del empleado

## Designs

**Inheritance:** each combination of pay type and commission is its own subclass
(`HourlyEmployee`, `HourlyEmployeeWithCommission`, ...). Six concrete classes in total.

**Composition:** there is a single `Employee` class that HAS-A `Contract` and MAY-HAVE-A
`Commission`. Any combination is built by passing different objects to the constructor.

> en herencia la formula de comision se repite 3 veces, en composicion solo una

## Requirements

Python 3.10 or newer. No external libraries.

## How to run

### Inheritance version

```bash
cd inheritance
python main.py
```

### Composition version

```bash
cd composition
python main.py
```

> en mac puede ser `python3` en lugar de `python`

## Expected output

Both versions print the same payroll (only the title line changes):

```
  1  Ana Lopez    $ 19,200.00
  2  Bruno Diaz   $ 25,000.00
  3  Carla Ruiz   $ 24,000.00
  4  Diego Mora   $ 17,000.00
  5  Elena Soto   $ 29,200.00
  6  Fer Nava     $ 24,000.00
```
