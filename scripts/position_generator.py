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


def generate_position():
    board = chess.Board("8/8/8/8/8/8/8/8 w - -")

    while(True):
        if (not board.is_valid()):
            board.clear()
            board.set_piece_at(chess.square(random.randint(0,7), random.randint(0,7)), chess.Piece(chess.KING, chess.BLACK))
            board.set_piece_at(chess.square(random.randint(0,7), random.randint(0,7)), chess.Piece(chess.KING, chess.WHITE))
            board.set_piece_at(chess.square(random.randint(0,7), random.randint(0,7)), chess.Piece(chess.ROOK, chess.WHITE))
        else:
            break
    print(list(board.legal_moves)[0])
    print(board)
    return board 

if __name__ == "__main__":  
    generate_position()
