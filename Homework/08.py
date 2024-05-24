'''複製+修改，複製LeeYi的程式，並且可成功執行'''

import gym

# 創建CartPole環境
env = gym.make("CartPole-v1")

# 重設環境並取得初始觀察
observation = env.reset()

# 初始化步數
steps = 0

for _ in range(1000):
    # 渲染環境
    env.render()

    # 根據觀察選擇動作
    if observation[2] > 0:
        action = 1  # 向右移動
    else:
        action = 0  # 向左移動

    # 執行動作，取得下一個觀察、獎勵、終止標誌和其他信息
    observation, reward, terminated, info = env.step(action)
    steps += 1
    print("step", steps)

    # 如果終止條件滿足，則重設環境並初始化步數
    if terminated:
        observation = env.reset()
        steps = 0
        print()

# 關閉環境
env.close()