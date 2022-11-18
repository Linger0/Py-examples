import numpy as np
import pandas as pd
import time

np.random.seed(2)  # reproducible

N_STATES = 6 # 一维世界的宽度
ACTIONS = ['left','right'] # 探索者可用的动作
EPSILON = 0.9 # greedy贪婪度
ALPHA = 0.1 # 学习率
GAMMA = 0.9 # 奖励递减值
MAX_EPISODES = 13 # 最大回合数
FRESH_TIME = 0.3 # 每回合移动间隔时间

def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),     # q_table 全 0 初始
        columns=actions,    # columns 对应的是行为名称
    )
    return table

# q_table:
"""
   left  right
0   0.0    0.0
1   0.0    0.0
2   0.0    0.0
3   0.0    0.0
4   0.0    0.0
5   0.0    0.0
"""

def choose_action(state, q_table):
    state_actions = q_table.iloc[state, :]  # 选出这个 state 的所有 action 的 value 值
    if (np.random.uniform() > EPSILON) or (state_actions.all() == 0):  # 非贪婪 or 或者这个 state 还没有探索过
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_actions.idxmax()    # 贪婪模式
    return action_name

def get_env_feedback(S,A):
    if A== 'right': # 往右探险
        if S == N_STATES - 2: # 找到宝藏
            S_ = 'terminal'
            R = 1
        else:
            S_ = S + 1
            R = 0
    else: # 往左探险
        R = 0
        if S == 0:
            S_ = S # 碰壁
        else:
            S_ = S - 1
    return S_,R

def update_env(S, episode, step_counter):
    env_list = ['-']*(N_STATES-1) + ['T']   # '---------T' our environment
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode+1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r                                ', end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)

def rl():
    q_table = build_q_table(N_STATES,ACTIONS) # 初始化 q_table
    for episode in range(MAX_EPISODES): # 回合
        step_counter = 0
        S = 0 # 回合初始的位置
        is_terminated = False
        update_env(S,episode,step_counter) # 环境更新
        while not is_terminated:

            A = choose_action(S,q_table) # 选择行为
            S_,R = get_env_feedback(S,A) # 实施行为并得到环境的反馈
            q_predict = q_table.loc[S,A] # 估算的（状态-行为）值
            if S_ != 'terminal':
                q_target = R + GAMMA*q_table.iloc[S_,:].max() # 实际的（状态-行为）值
            else:
                q_target = R # 实际的（状态-行为值）
                is_terminated = True

            q_table.loc[S,A] += ALPHA*(q_target - q_predict) # q_table 更新
            S = S_ # 更新探索者位置

            update_env(S,episode,step_counter+1)

            step_counter += 1
    return q_table

if __name__ == '__main__':
    rl()