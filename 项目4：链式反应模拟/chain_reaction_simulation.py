import numpy as np
import matplotlib.pyplot as plt

def chain_reaction_simulation(neutron_initial, fission_probability, steps):
    """
    链式反应模拟函数
    
    参数:
    neutron_initial -- 初始中子数量
    fission_probability -- 裂变概率 (每个中子引发新反应的概率)
    steps -- 仿真步骤数
    
    返回:
    neutron_counts -- 每个步骤的中子数量
    """
    neutron_counts = [neutron_initial]
    
    for _ in range(steps):
        current_neutrons = neutron_counts[-1]
        # 每个中子都有概率引发新反应
        new_neutrons = 0
        for _ in range(current_neutrons):
            if np.random.random() < fission_probability:
                # 每个成功反应产生2个新中子
                new_neutrons += 2
        neutron_counts.append(new_neutrons)
        
        # 如果中子数量为0，则反应终止
        if new_neutrons == 0:
            break
            
    return neutron_counts

def analyze_parameters():
    """
    分析不同参数对链式反应结果的影响
    """
    # 参数设置
    initial_neutron = 1
    fission_probabilities = [0.4, 0.5, 0.6]
    steps = 20
    
    # 对不同参数进行模拟
    results = {}
    for prob in fission_probabilities:
        result = chain_reaction_simulation(initial_neutron, prob, steps)
        results[prob] = result
        
    # 绘制结果
    plt.figure(figsize=(10, 6))
    for prob, counts in results.items():
        plt.plot(counts, label=f'裂变概率={prob}')
        
    plt.xlabel('reaction step')
    plt.ylabel('The number of neutrons')
    plt.title('The influence of different fission probabilities on chain reactions')
    plt.legend()
    plt.grid()
    plt.show()
    
    # 分析结果
    print("链式反应分析结果:")
    for prob in fission_probabilities:
        counts = results[prob]
        print(f"\n裂变概率={prob}:")
        print(f" - 最大中子数量: {max(counts)}")
        print(f" - 链式反应持续步数: {len(counts)}")
        print(f" - 反应终止原因: {'中子耗尽' if counts[-1] == 0 else '达到最大步数'}")

if __name__ == "__main__":
    analyze_parameters()
