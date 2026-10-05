#FEN BASICS
#Lowercase letters describe the black pieces. Just like in PGN, "p" stands for pawn, "r" for rook, "n" for knight, 
# "b" for bishop, "q" for queen, and "k" for king. The same letters are used for the white pieces, but they appear in uppercase. 
# Empty squares are denoted by numbers from one to eight, depending on how many empty squares are between two pieces.

#The second field indicates who moves next. This field always appears in lowercase, and "w" specifies that it 
# is White's turn to move, while "b" indicates that Black plays next.

#The letter "k" indicates that kingside castling is available, while "q" means that a player may castle queenside. 
#The symbol "-" designates that neither side may castle. 


import chess
import random
import itertools
import chess.gaviota
tablebase = chess.gaviota.open_tablebase(r"C:\Users\user\Desktop\projects\RL-RookMate\chess_env")

def generate_position(max_dtm = 7):
    while True:
        wk, wq, bk = random.sample(range(64), 3)      # distinct squares
        board = chess.Board(None)
        board.set_piece_at(wk, chess.Piece(chess.KING, chess.WHITE))
        board.set_piece_at(wq, chess.Piece(chess.QUEEN, chess.WHITE))
        board.set_piece_at(bk, chess.Piece(chess.KING, chess.BLACK))
        board.turn = chess.WHITE

        if not board.is_valid() or board.is_game_over():
            continue
        if max_dtm is not None:
            dtm = tablebase.probe_dtm(board)
            if not (0 < dtm <= max_dtm):
                continue
        return board.fen()


if __name__ == "__main__":  
    print(chess.Board(generate_position()))
