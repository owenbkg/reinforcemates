from enum import Enum
import gymnasium as gym
from gymnasium import spaces
import numpy as np
import chess
import random

from chess_env.position_generator import generate_position 


class chessEnv(gym.Env):
    metadata = {"render_modes": ["ansi"]}    

    def __init__(self, start_fen=None, max_moves = 50):
        self.start_fen = start_fen
        self.board = None
        self.observation_space = spaces.Box(0, 1, shape=(3, 8, 8), dtype=np.int8)
        self.action_space = spaces.Discrete(4096)
        self.n_moves = 0
        self.max_moves = max_moves

    def _get_obs(self):
        #example output: {60: Piece.from_symbol('R'), 47: Piece.from_symbol('k'), 5: Piece.from_symbol('K')}
        piece_dict = self.board.piece_map()
        obs_arr = np.zeros((3,8,8), dtype = np.int8)
        i = 0
        for coord, piece in piece_dict.items():
            if piece.color == chess.BLACK:
                plane  = 2
            elif piece.piece_type == chess.KING:
                plane = 0
            else:
                plane = 1
            rank = chess.square_rank(coord)
            file = chess.square_file(coord)
            obs_arr[plane, rank, file] = 1
            i += 1

        return obs_arr


    def _get_info(self):
        return {"fen": self.board.fen()}

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        fen = self.start_fen if self.start_fen is not None else generate_position()
        self.board = chess.Board(fen)      
        self.n_moves = 0
        return self._get_obs(), self._get_info()
            
    def step(self, action):
        from_square = action//64
        to_square = action % 64
        #legal move check
        move = chess.Move(from_square, to_square)
        if self.board.is_legal(move):
            self.board.push(move)       
        else:
            raise ValueError(f"Illegal move {action}")     
        if self.board.is_checkmate():
            return self._get_obs(), 1.0, True, False, self._get_info()
        elif self.board.is_stalemate():
            return self._get_obs(), -0.5, True, False, self._get_info()


        #black makes a move
        moves = list(self.board.legal_moves)
        move = moves[random.randint(0,len(moves)-1)]
        self.board.push(move)

        self.n_moves+=1
        truncated = self.n_moves >= self.max_moves

        if self.board.is_game_over():    
            return self._get_obs(), -0.5, True, False, self._get_info()
        return self._get_obs()   , -0.05, False, truncated, self._get_info()


    def render(self):
        return self.board

    def _render_frame(self):
        return

    def close(self):
        return
    
    def action_mask(self):
        mask = np.zeros(4096, dtype=bool)
        for move in self.board.legal_moves:
            mask[move.from_square * 64 + move.to_square] = True
        return mask