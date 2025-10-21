# Load Balancing Simulation - First Fit Algorithm

# Step 1: Initialize processors and tasks
processors = [0, 0, 0]  # total load on each processor (3 processors)
tasks = [5, 2, 8, 3, 7]  # workload of each task

# Step 2: Assign each task
for i, task in enumerate(tasks):
    # find the processor with the least load
    min_index = processors.index(min(processors))
    # assign the task to that processor
    processors[min_index] += task
    print(f"Task {i+1} (load={task}) assigned to Processor {min_index+1}")

# Step 3: Display final processor loads
print("\nFinal Processor Loads:")
for i, load in enumerate(processors):
    print(f"Processor {i+1}: {load}")
