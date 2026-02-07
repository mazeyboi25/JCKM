import threading
import time

def compute_subject_gwa(grade, index, results):
    time.sleep(0.1) 
    print(f"[Thread-{index}] Subject {index + 1} grade = {grade}")
    results[index] = grade

if __name__ == "__main__":
    n = int(input("Enter number of subjects: "))
    grades = []

    for i in range(n):
        grade = float(input(f"Enter grade for subject {i + 1}: "))
        grades.append(grade)

    results = {}
    threads = []

    start_time = time.time()

    for i, grade in enumerate(grades):
        t = threading.Thread(
            target=compute_subject_gwa,
            args=(grade, i, results)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    gwa = sum(results.values()) / len(results)

    end_time = time.time()

    print("\nAll threads finished.")
    print(f"Overall GWA (all subjects): {gwa:.2f}")
    print(f"Multithreading Execution Time: {end_time - start_time:.4f} seconds")
