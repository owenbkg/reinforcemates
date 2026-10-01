import chess
import gymnasium as gym
import sys
sys.path.append(r"C:\Users\user\Desktop\projects\RL-RookMate\chess_env\envs")
from chessEnv import chessEnv


gym.register(
    id="chess_env/ChessEnv-v0",
    entry_point=chessEnv,
    max_episode_steps=300,  # Prevent infinite episodes
)

env = gym.make("chess_env/ChessEnv-v0",
               start_fen="4k3/R7/4K3/8/8/8/8/8 w - - 0 1")
obs = env.reset(seed=0)
print(env.unwrapped.board)

move = chess.Move.from_uci("a7a8")
action = move.from_square * 64 + move.to_square   # 48*64 + 56 = 3128

obs, reward, terminated, truncated, info = env.step(action)
print(reward, terminated, truncated)
print(env.unwrapped.board.is_checkmate())