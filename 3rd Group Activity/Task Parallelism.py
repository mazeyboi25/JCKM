from concurrent.futures import ThreadPoolExecutor
import threading

# Sample salary
salary = 50000


# 1️⃣ Define four independent deduction functions

def compute_sss(salary):
    print(f"SSS computed by {threading.current_thread().name}")
    return salary * 0.045  # example 4.5%

def compute_philhealth(salary):
    print(f"PhilHealth computed by {threading.current_thread().name}")
    return salary * 0.035  # example 3.5%

def compute_pagibig(salary):
    print(f"Pag-IBIG computed by {threading.current_thread().name}")
    return salary * 0.02  # example 2%

def compute_withholding_tax(salary):
    print(f"Withholding Tax computed by {threading.current_thread().name}")
    return salary * 0.10  # example 10%


# 2️⃣ Use ThreadPoolExecutor to run them concurrently
with ThreadPoolExecutor(max_workers=4) as executor:
    future_sss = executor.submit(compute_sss, salary)
    future_philhealth = executor.submit(compute_philhealth, salary)
    future_pagibig = executor.submit(compute_pagibig, salary)
    future_tax = executor.submit(compute_withholding_tax, salary)

    # 3️⃣ Retrieve results using Future objects
    sss = future_sss.result()
    philhealth = future_philhealth.result()
    pagibig = future_pagibig.result()
    tax = future_tax.result()

print("Results retrieved successfully.")
