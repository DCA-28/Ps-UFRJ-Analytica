import pandas as pd

""" Operators will be a list containing the indexes of all the virtually possible horse movements, for example the 
    horse can go 2 places up and 1 place left, witch is accomplished by the operator: [2, -1]. That moviment is realized 
    by adding these opperator numbers to the horizontal coordinate (hori_coord) and vertical coordinate (vert_coord). 
    In that case we would have: final_vert = vert_coord + 2 and final_hori = hori_coord - 1. Given the starting position 
    of the horse and using all the operators on that position, we have virtually all end positions. These end positions
    are analyzed in the future to find only the valid ones."""

""" The symbols on the board that will be printed indicate:
    h -> the horse position
    o -> one of the houses the horse can go
    * -> the final position of the horse (when it exists)"""


def all_moves(position: str) -> str:
    hori_coord = position[0]  # represents the letter in the position (horizontal coordinate)
    vert_coord = position[1]  # represents the number in the position (vertical coordinate)
    possible_coords = []

    operators = [[2, -1], [2, 1], [1, -2], [1, 2], [-2, -1], [-2, 1], [-1, -2], [-1, 2]]

    for operator in operators:
        final_vert = (ord(vert_coord) + operator[0])  # final vertical coordinate after applying the vertical move
        final_hori = (ord(hori_coord) + operator[1])  # final horizontal coordinate after applying the vertical move
        final_cords = chr(final_hori) + chr(final_vert)
        possible_coords.append(final_cords)
    return possible_coords


def possible_moves(possible_coords: list) -> list:
    possible_moves = []
    for coordinates in possible_coords:
        hori_coord = coordinates[0]
        verti_coord = coordinates[1]
        if (ord(hori_coord) > 104 or ord(hori_coord) < 97):  # whether the horse has crossed the left or right limit
            continue
        elif (ord(verti_coord) > 56 or ord(verti_coord) < 49):  # whether the horse has crossed the upper or lower limit
            continue
        else:
            possible_moves.append((coordinates))
    return possible_moves


class ChessBoard:
    def __init__(self) -> None:
        self.board = pd.DataFrame(
            {
                "a": [".", ".", ".", ".", ".", ".", ".", "."],
                "b": [".", ".", ".", ".", ".", ".", ".", "."],
                "c": [".", ".", ".", ".", ".", ".", ".", "."],
                "d": [".", ".", ".", ".", ".", ".", ".", "."],
                "e": [".", ".", ".", ".", ".", ".", ".", "."],
                "f": [".", ".", ".", ".", ".", ".", ".", "."],
                "g": [".", ".", ".", ".", ".", ".", ".", "."],
                "h": [".", ".", ".", ".", ".", ".", ".", "."],
            },
            index=[i + 1 for i in range(8)],
        )

    def stamp_moves(self, initial_pos, final_pos, moves: list) -> None:
        self.board[initial_pos[0]][int(initial_pos[1])] = "h"  # marking the horse start position
        for move in moves:
            if move == final_pos:
                self.board[move[0]][int(move[1])] = "*"
            else:
                self.board[move[0]][int(move[1])] = "o"

    def get_board(self) -> "board":
        return self.board

def main():
    initial_pos, final_pos = input().split()
    moves = all_moves(initial_pos)
    valid_moves = possible_moves(moves)
    # creating the chess board, stamping the moves on it and printing this board
    board = ChessBoard()
    board.stamp_moves(initial_pos, final_pos, valid_moves)
    marked_places = board.get_board()
    if final_pos in valid_moves:
        print("O movimento é válido,\nA casa final pode ser alcançada pelo cavalo:\n")
    else:
        print("O movimento é inválido,\nObservamos que a casa final não pode ser alcançada pelo cavalo:\n")
    print(marked_places)

main()
