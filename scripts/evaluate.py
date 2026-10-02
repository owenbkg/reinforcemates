import gymnasium as gym
from sb3_contrib import MaskablePPO
from sb3_contrib.common.maskable.evaluation import evaluate_policy
from sb3_contrib.common.wrappers import ActionMasker
from stable_baselines3.common.monitor import Monitor
import numpy as np

import chess_env

def mask_fn(env):
    return env.unwrapped.action_mask()


if __name__ == "__main__":
    env = gym.make("chess_env/ChessEnv-v0")
    env = Monitor(ActionMasker(env, mask_fn))
    model = MaskablePPO.load("checkpoints/ppo_kqk", env=env)


    reward_mean, std = evaluate_policy(
        model, env, n_eval_episodes=100, deterministic=True)

    print(reward_mean, std)