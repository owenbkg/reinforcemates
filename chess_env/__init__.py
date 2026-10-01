from gymnasium.envs.registration import register

register(
    id="chess-env/GridWorld-v0",
    entry_point="chess-env.envs:GridWorldEnv",
)
