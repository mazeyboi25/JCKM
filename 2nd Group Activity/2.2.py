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
                
# Each subject grade in the multiprocessing version is handled by a separate process that runs independently from the others.
# When all processes are started, the operating system schedules them to run in parallel, so their execution and completion
# times may vary. This causes the output to appear in a non-deterministic order, with each process printing its result as soon
# as it finishes. After all processes have completed, the main process collects the results and computes the final GWA,
# ensuring that all subject grades are included in the final output.

    