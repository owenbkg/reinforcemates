import gymnasium as gym
from sb3_contrib import MaskablePPO
from sb3_contrib.common.wrappers import ActionMasker
from stable_baselines3.common.env_util import make_vec_env

import chess_env  


def mask_fn(env):
    return env.unwrapped.action_mask()

if __name__ == "__main__":
    vec_env = make_vec_env(
        "chess_env/ChessEnv-v0",
        n_envs=5,
        wrapper_class=ActionMasker,
        wrapper_kwargs={"action_mask_fn": mask_fn},
    )
    model = MaskablePPO("MlpPolicy", vec_env, gamma=0.9, verbose=1)
    model.learn(total_timesteps=10_000)
    model.save("checkpoints/ppo_krk")

    """
    env = gym.make("chess_env/ChessEnv-v0",
                start_fen="4k3/R7/4K3/8/8/8/8/8 w - - 0 1")
    obs = env.reset(seed=0)
    print(env.unwrapped.board)

    move = chess.Move.from_uci("a7a8")
    action = move.from_square * 64 + move.to_square   # 48*64 + 56 = 3128

    obs, reward, terminated, truncated, info = env.step(action)
    print(reward, terminated, truncated)
    print(env.unwrapped.board.is_checkmate())
    """

