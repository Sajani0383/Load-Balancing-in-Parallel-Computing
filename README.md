# ⚙️ Load Balancing in Parallel Computing Systems

### 👩‍💻 Author: **Sajani G**
### 🎓 Academic Project | Python Simulation

---

## 🧠 Project Overview

This project simulates **load balancing in parallel computing systems**, where multiple processors share workloads to achieve efficient execution and minimize performance bottlenecks.

The simulation demonstrates three classical **load balancing algorithms**:

1. 🟦 **First-Fit**
2. 🟨 **Best-Fit**
3. 🟩 **Worst-Fit**

Each algorithm distributes a set of tasks (each with a workload value) across multiple processors and compares their efficiency using a graphical analysis.

---

## 🎯 **Aim**

To simulate and compare the performance of First-Fit, Best-Fit, and Worst-Fit load balancing algorithms in parallel computing systems using Python.

---

## 🧩 **Project Description**

Load balancing ensures that all processors in a system are utilized efficiently by distributing workloads evenly.  
When one processor is overloaded while others are idle, system performance degrades.  
This project demonstrates how different load balancing algorithms manage this challenge.

### ⚙️ Simulation Process
- A list of tasks with specific workload values is defined.
- Multiple processors (e.g., 3 processors) are available.
- Each algorithm assigns tasks differently to achieve balanced processor loads.
- The final load on each processor is calculated and visualized using **Matplotlib**.

---

## 🧮 **Algorithms Implemented**

### 🔹 1. First-Fit Algorithm
- Assigns each new task to the **least loaded processor** at that moment.
- Simple and fast but may not always produce the most balanced distribution.

### 🔹 2. Best-Fit Algorithm
- Calculates the **future load** on each processor after task assignment.
- Chooses the processor that leads to the **most balanced total load**.
- Usually provides better load balance.

### 🔹 3. Worst-Fit Algorithm
- Assigns each new task to the processor that currently has the **most available capacity**.
- Spreads tasks widely in the beginning but can lead to imbalance in some cases.

---

## 💻 **Implementation**

### 🐍 Language & Tools
- **Python 3.11+**
- **Matplotlib** library (for graph visualization)

### 🧠 Code Structure
load_balancing_simulation.py
│
├── first_fit() → Implements the First-Fit algorithm
├── best_fit() → Implements the Best-Fit algorithm
├── worst_fit() → Implements the Worst-Fit algorithm
└── simulate_load_balancing() → Executes and visualizes results
