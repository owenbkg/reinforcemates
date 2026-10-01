from chess_env.envs.chessEnv import chessEnv

def __init__(self, render_mode=None, max_moves=50):
    super().__init__()
    self.observation_space = spaces.Box(low=0, high=1, shape=(3, 8, 8), dtype=np.int8)
    self.action_space = spaces.Discrete(4096)