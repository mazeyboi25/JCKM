from multiprocessing import Process, Manager
import time

def compute_gwa_process(grades, results, index):
    time.sleep(0.1)  # simulate work
    gwa = sum(grades) / len(grades)
    results[index] = gwa
    print(f"[Process-{index}] GWA = {gwa:.2f}")

if __name__ == "__main__":
    n = int(input("Enter number of subjects: "))
    grades = []

    for i in range(n):
        grade = float(input(f"Enter grade for subject {i+1}: "))
        grades.append(grade)

    manager = Manager()
    results = manager.dict()
    processes = []

    start_time = time.time()

    for i in range(len(grades)):
        p = Process(
            target=compute_gwa_process,
            args=([grades[i]], results, i)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()

    print("\nMultiprocessing Execution Time:",
          end_time - start_time, "seconds")
                
    print("Final GWA:", sum(results.values()) / len(results))
 
                
# In the multiprocessing approach, each subject grade is processed by its own independent process.
# Once all processes are launched, the operating system manages their parallel execution, which means
# they may start and finish at different times. As a result, the order of the printed outputs is not fixed,
# since each process displays its result immediately after completing its task. After every process has
# finished running, the main process gathers all computed values and calculates the final GWA, ensuring
# that all subject grades are reflected in the final result.

    