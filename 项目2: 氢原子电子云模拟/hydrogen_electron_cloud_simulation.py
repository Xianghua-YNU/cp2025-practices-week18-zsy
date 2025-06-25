import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 物理常数和参数
a0 = 5.29e-2  # 博尔半径，单位 nm
r0 = 0.25     # 收敛半径，单位 nm
n_points = 10000  # 电子点数

# 电子云分布概率密度函数
def electron_cloud_probability(r):
    return (4 * r**2 / a0**3) * np.exp(-2 * r / a0)

# 模拟电子云分布
def simulate_electron_cloud(n_points):
    # 根据概率密度函数随机采样半径
    r = np.linspace(0, r0, 1000)
    probabilities = electron_cloud_probability(r)
    probabilities /= probabilities.sum()  # 归一化概率密度
    
    # 根据概率密度分布随机选择点的半径
    selected_r = np.random.choice(r, size=n_points, p=probabilities)
    
    # 随机生成球坐标系中的角度θ和φ
    theta = np.random.uniform(0, np.pi, n_points)
    phi = np.random.uniform(0, 2 * np.pi, n_points)
    
    # 转换为笛卡尔坐标
    x = selected_r * np.sin(theta) * np.cos(phi)
    y = selected_r * np.sin(theta) * np.sin(phi)
    z = selected_r * np.cos(theta)
    
    return x, y, z

# 可视化电子云分布
def visualize_electron_cloud(x, y, z):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 绘制电子云点
    ax.scatter(x, y, z, s=2, alpha=0.6, c='blue', marker='o')
    
    # 设置坐标轴标签和标题
    ax.set_xlabel('X (nm)')
    ax.set_ylabel('Y (nm)')
    ax.set_zlabel('Z (nm)')
    ax.set_title('Distribution of the electron cloud in the ground state of a hydrogen atom', fontsize=14)
    
    # 设置坐标轴范围
    ax.set_xlim(-r0, r0)
    ax.set_ylim(-r0, r0)
    ax.set_zlim(-r0, r0)
    
    plt.show()
    plt.savefig('Distribution of the electron cloud in the ground state of a hydrogen atom')

# 执行模拟和可视化
x, y, z = simulate_electron_cloud(n_points)
visualize_electron_cloud(x, y, z)

# 分析不同参数对电子云分布的影响
def analyze_parameters():
    print("参数分析:")
    print("1. 博尔半径 (a0): 决定了电子云的扩散程度，a0越大，电子云越扩散")
    print("2. 收敛半径 (r0): 影响可视化效果，通常设置为可展示电子云主要分布区域的半径")
    print("3. 点数 (n_points): 决定了模拟的精度，点数越多，越接近真实分布")
    print("4. 概率密度函数形式: 由氢原子基态的量子力学性质决定，决定了电子云的形状")

analyze_parameters()
