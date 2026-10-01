from gymnasium.envs.registration import register

register(
    id="chess_env/ChessEnv-v0",
    entry_point="chess_env.envs.chessEnv:chessEnv",
    max_episode_steps=300,
)