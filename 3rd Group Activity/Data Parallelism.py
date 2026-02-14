from concurrent.futures import ProcessPoolExecutor

# Deduction rates
SSS_RATE = 0.050
PHILHEALTH_RATE = 0.060
PAGIBIG_RATE = 0.10
TAX_RATE = 0.30

# Given employees
employees = [
    ("Jeff", 25000000),
    ("Cielo", 32000000),
    ("Kyle", 28000000),
    ("Meinard", 50000000),
    ("Yasser", 100000000)
]

def compute_payroll(employee):
    name, salary = employee

    sss = salary * SSS_RATE
    philhealth = salary * PHILHEALTH_RATE
    pagibig = salary * PAGIBIG_RATE
    tax = salary * TAX_RATE

    total_deduction = sss + philhealth + pagibig + tax
    net_salary = salary - total_deduction

    return (name, salary, total_deduction, net_salary)

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = executor.map(compute_payroll, employees)

        for name, salary, total_deduction, net_salary in results:
            print(f"\nEmployee: {name}")
            print(f"Gross Salary: ₱{salary:,.2f}")
            print(f"Total Deduction: ₱{total_deduction:,.2f}")
            print(f"Net Salary: ₱{net_salary:,.2f}")
