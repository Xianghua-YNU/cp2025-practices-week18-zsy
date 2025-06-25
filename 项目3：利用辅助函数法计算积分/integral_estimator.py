import numpy as np

# 定义被积函数和权重函数
def integrand(x):
    return x**(-1/2) / (np.exp(x) + 1)

def weight(x):
    return 1 / (2 * np.sqrt(x))

# 导出满足权重分布的随机数生成公式
# 累积分布函数 F(x) = ∫₀^x p(t)dt = ∫₀^x [1/(2√t)] dt = √x
# 要生成符合这个分布的随机数，可以使用逆变换法：
# 设 u 是 [0,1) 上的均匀随机数，则 x = F⁻¹(u) = u²
def generate_random_samples(N):
    u = np.random.uniform(0, 1, N)
    x = u ** 2
    return x

# 蒙特卡洛积分
N = 1000000  # 样本数量
x = generate_random_samples(N)
f = integrand(x)
p = weight(x)

# 积分估计
I_estimate = np.mean(f / p)

# 统计误差估计
var_f = np.mean((f / p)**2) - I_estimate**2
sigma = np.sqrt(var_f / N)

print(f"积分估计值: {I_estimate:.4f}")
print(f"统计误差估计: {sigma:.4f}")
