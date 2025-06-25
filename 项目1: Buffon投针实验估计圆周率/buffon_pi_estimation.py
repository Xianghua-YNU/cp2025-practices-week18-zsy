import random
import math
import matplotlib.pyplot as plt

def buffon_needle_experiment(num_trials, needle_length=1.0, line_spacing=1.0):
    intersections = 0
    for _ in range(num_trials):
        x = random.uniform(0, line_spacing / 2)
        theta = random.uniform(0, math.pi)
        if x <= (needle_length / 2) * math.sin(theta):
            intersections += 1
    pi_estimate = (2.0 * needle_length * num_trials) / (line_spacing * intersections) if intersections > 0 else float('inf')
    return pi_estimate

def analyze_experiment():
    experiment_counts = [100, 1000, 10000, 100000, 1000000]
    pi_estimates = []
    errors = []
    
    print("实验次数\tπ估计值\t误差百分比")
    for n in experiment_counts:
        pi = buffon_needle_experiment(n)
        error = abs(pi - math.pi) / math.pi * 100
        pi_estimates.append(pi)
        errors.append(error)
        
        print(f"{n}\t{pi:.6f}\t{error:.4f}%")
    
    plt.figure(figsize=(10, 6))
    plt.plot(experiment_counts, pi_estimates, marker='o')
    plt.axhline(math.pi, color='r', linestyle='--', label='true value')
    plt.xscale('log')
    plt.xlabel('number of experiment')
    plt.ylabel('Estimated value of π')
    plt.title('The influence of the number of experiments on the estimated value of π')
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.savefig('The influence of the number of experiments on the estimated value of π')

    plt.figure(figsize=(10, 6))
    plt.loglog(experiment_counts, errors, marker='o', base=10)
    plt.xlabel('Number of experiments (logarithmic scale)')
    plt.ylabel('Relative error (%) (logarithmic scale)')
    plt.title('The relationship between the number of experiments and the error')
    plt.grid(True)
    plt.show()
    plt.savefig('The relationship between the number of experiments and the error')

if __name__ == "__main__":
    analyze_experiment()
