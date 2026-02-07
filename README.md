3. Table
| Method           | Execution Order                | GWA Output                             | Execution Time |
|------------------|--------------------------------|----------------------------------------|----------------|
| Multithreading   | 3 -> 1 -> 4 -> 2 -> 5 (Random) |  2.12, 88.75, 91.00, 84.00, 76.25      |Average = 0.5144 ÷ 5 = 0.10288 
| Multiprocessing  | Non-deterministic              | Correct GWA displayed |                |

- 


4. README.md Questions
1. Which approach demonstrates true parallelism in Python? Explain.
- Multiprocessing demonstrates true parallelism in Python because each process has its own Python interpreter and CPU core, avoiding the Global Interpreter Lock (GIL).
2. Compare execution times between multithreading and multiprocessing.
- Multiprocessing usually has a longer startup time than multithreading, but it performs better for CPU-bound tasks because computations run in parallel.
3. Can Python handle true parallelism using threads? Why or why not?
- Python cannot achieve true parallelism using threads for CPU-bound tasks due to the Global Interpreter Lock, which allows only one thread to execute Python bytecode at a time.
4. What happens if you input a large number of grades (e.g., 1000)? Which
method is faster and why?
- When a large number of grades (e.g., 1000) is used, multiprocessing becomes faster for heavy computations, while multithreading becomes slower due to context switching and GIL limitations.
5. Which method is better for CPU-bound tasks and which for I/O-bound
tasks?
- Multiprocessing is better for CPU-bound tasks, while multithreading is better for I/O-bound tasks such as file reading or network requests.
6. How did your group apply creative coding or algorithmic solutions in this
lab?    
- Creativity was applied by adding execution timing, simulated workload delays, shared result storage, and dynamic user input to clearly demonstrate behavioral and performance differences.