# Load Balancing Simulation - Best Fit Algorithm

processors = [0, 0, 0]  # workload on each processor
tasks = [5, 2, 8, 3, 7]  # workloads for each task

for i, task in enumerate(tasks):
    # Step 1: Find the processor that will have the smallest load after assigning this task
    best_index = 0
    best_future_load = processors[0] + task
    
    for j in range(1, len(processors)):
        future_load = processors[j] + task
        # choose the processor with the smallest future load
        if future_load < best_future_load:
            best_future_load = future_load
            best_index = j
    
    # Step 2: Assign the task to that processor
    processors[best_index] += task
    print(f"Task {i+1} (load={task}) assigned to Processor {best_index+1}")

# Step 3: Display final processor loads
print("\nFinal Processor Loads:")
for i, load in enumerate(processors):
    print(f"Processor {i+1}: {load}")
