# Load Balancing Simulation - Worst Fit Algorithm

processors = [0, 0, 0]  # workload on each processor
tasks = [5, 2, 8, 3, 7]  # workloads for each task

for i, task in enumerate(tasks):
    # Step 1: Find the processor with the least current load
    min_index = processors.index(min(processors))
    # Step 2: Assign the task to that processor
    processors[min_index] += task
    print(f"Task {i+1} (load={task}) assigned to Processor {min_index+1}")

# Step 3: Display final processor loads
print("\nFinal Processor Loads:")
for i, load in enumerate(processors):
    print(f"Processor {i+1}: {load}")
