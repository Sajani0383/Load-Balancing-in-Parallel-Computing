# ===============================================
# LOAD BALANCING IN PARALLEL COMPUTING SYSTEMS
# ===============================================
# Author: Sajani G
# Language: Python
# Libraries: Matplotlib
# Description:
# Simulate workload distribution among multiple processors
# using three load balancing algorithms — First-Fit, Best-Fit, and Worst-Fit.
# Compare their performance visually with a bar graph.

import matplotlib.pyplot as plt

# ---------- Algorithm 1: FIRST-FIT ----------
# Assign each new task to the processor with the least current load.
def first_fit(tasks, num_processors):
    processors = [0] * num_processors
    for task in tasks:
        # Always pick the first processor with least load
        min_index = processors.index(min(processors))
        processors[min_index] += task
    return processors


def best_fit(tasks, num_processors):
    processors = [0] * num_processors
    for task in tasks:
        # Choose processor that will have the smallest load AFTER assignment
        best_index = 0
        smallest_diff = float('inf')
        for i in range(num_processors):
            diff = abs((processors[i] + task) - (sum(processors) / num_processors))
            if diff < smallest_diff:
                smallest_diff = diff
                best_index = i
        processors[best_index] += task
    return processors


def worst_fit(tasks, num_processors):
    processors = [0] * num_processors
    for task in tasks:
        # Find processor with LEAST current load
        min_index = processors.index(min(processors))
        processors[min_index] += task
    return processors



# ---------- MAIN SIMULATION FUNCTION ----------
def simulate_load_balancing(tasks, num_processors):
    print("=====================================")
    print("LOAD BALANCING SIMULATION")
    print("=====================================")
    print(f"Tasks: {tasks}")
    print(f"Number of Processors: {num_processors}\n")

    # Run all three algorithms
    first_result = first_fit(tasks, num_processors)
    best_result = best_fit(tasks, num_processors)
    worst_result = worst_fit(tasks, num_processors)

    # Display results
    print("Final Processor Loads:")
    print(f"First-Fit: {first_result}")
    print(f"Best-Fit:  {best_result}")
    print(f"Worst-Fit: {worst_result}")

    # ---------- Visualization ----------
    labels = [f"P{i+1}" for i in range(num_processors)]
    x = range(num_processors)

    plt.figure(figsize=(9, 6))
    plt.bar([i - 0.25 for i in x], first_result, width=0.25, label='First-Fit')
    plt.bar(x, best_result, width=0.25, label='Best-Fit')
    plt.bar([i + 0.25 for i in x], worst_result, width=0.25, label='Worst-Fit')

    plt.xlabel("Processors")
    plt.ylabel("Total Workload")
    plt.title("Comparison of Load Balancing Algorithms")
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


# ---------- RUN THE SIMULATION ----------
# You can modify these values for testing.
tasks = [20, 10, 5, 15, 25, 5, 30]
num_processors = 3

simulate_load_balancing(tasks, num_processors)

