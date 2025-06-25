import random
import math
import matplotlib.pyplot as plt
import numpy as np

def buffon_needle_experiment(num_trials, needle_length=1.0, line_spacing=1.0):
    """
    模拟 Buffon 投针实验
    
    参数:
    num_trials -- 实验次数
    needle_length -- 针的长度
    line_spacing -- 平行线之间的间距
    
    返回:
    pi_estimate -- π 的估计值
    intersections -- 相交次数
    """
    intersections = 0
    
    # 进行多次投针试验
    for _ in range(num_trials):
        # 随机生成针的中心位置 (0 到线间距的一半之间)
        x = random.uniform(0, line_spacing / 2)
        
        # 随机生成针的角度 (0 到 π 之间)
        theta = random.uniform(0, math.pi)
        
        # 判断针是否与线相交
        if x <= (needle_length / 2) * math.sin(theta):
            intersections += 1
    
    # 计算π的估计值
    if intersections > 0:
        pi_estimate = (2.0 * needle_length * num_trials) / (line_spacing * intersections)
    else:
        pi_estimate = float('inf')  # 避免除零错误
    
    return pi_estimate, intersections

def analyze_experiment():
    """
    运行实验并分析结果
    """
    # 保持线间距和针长相同，这是标准的 Buffon 投针问题
    line_spacing = 1.0
    needle_length = line_spacing
    
    print("Buffon 投针实验估计 π 值")
    print("==========================")
    
    # 运行一次大样本实验
    num_trials = 10000000  # 实验次数
    pi_estimate, intersections = buffon_needle_experiment(num_trials)
    
    print(f"\n实验次数: {num_trials}")
    print(f"相交次数: {intersections}")
    print(f"π 的估计值: {pi_estimate}")
    print(f"与真实值的误差百分比: {abs(pi_estimate - math.pi)/math.pi * 100:.6f}%")
    
    # 分析实验次数对精度的影响
    print("\n实验次数对估计精度的影响分析:")
    trials_list = [100, 1000, 10000, 100000, 1000000, 10000000]
    errors = []
    
    for trials in trials_list:
        avg_pi = 0.0
        num_repeats = 5  # 对每个实验次数重复多次取平均
        for _ in range(num_repeats):
            avg_pi += buffon_needle_experiment(trials)[0]
        avg_pi /= num_repeats
        
        error = abs(avg_pi - math.pi)/math.pi * 100
        errors.append(error)
        
        print(f"实验次数: {trials}, 平均π估计值: {avg_pi:.6f}, 误差百分比: {error:.6f}%")
    
    # 绘制误差与实验次数的关系图
    plt.figure(figsize=(10, 6))
    plt.loglog(trials_list, errors, 'o-', basex=10, basey=10)
    plt.xlabel('Number of experiments (logarithmic scale)')
    plt.ylabel('Relative error (%) (logarithmic scale)')
    plt.title('The Relationship between the Number of Experiments and the Precision of π Estimation')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    analyze_experiment()
