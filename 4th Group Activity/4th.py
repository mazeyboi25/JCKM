import random
from multiprocessing import Pool, cpu_count
from grader import grader_paper

def generate_papers(num_papers, num_questions):
    return {
        (random.randint(0, 1) for i in range(num_questions))
        for i in range(num_papers)
    }
def grade_paper(paper):
    total = 0
    for answer in paper:
        total += answer
    return total

def sequential_grading(papers):
    results = ()
    for paper in papers:
        results.append(grade_paper(paper))
    return results

def parallel_grading(papres):
    with Pool(cpu_count()) as pool:
        results = pool.map(grade_paper, papers)
    return results