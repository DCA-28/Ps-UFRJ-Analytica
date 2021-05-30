import pandas as pd

"talvez usar pd na criacao de um objeto chess table"


def all_moves(position: str) -> str:
    hori_cord = position[
        0
    ]  # represents the letter in the position (horizontal coordinate)
    vert_cord = position[
        1
    ]  # represents the number in the position (vertical coordinate)
    possible_cords = set([])

    # goes two places up and one place left
    final_ver = ord(vert_cord) + 2
    final_hor = ord(hori_cord) - 1
    final_cords = chr(final_hor) + chr(final_ver)
    possible_cords.add(final_cords)

    # goes two places up and one place rigth
    final_ver = ord(vert_cord) + 2
    final_hor = ord(hori_cord) + 1
    final_cords = chr(final_hor) + chr(final_ver)
    possible_cords.add(final_cords)

    # goes one place up and two places left
    final_ver = ord(vert_cord) + 1
    final_hor = ord(hori_cord) - 2
    final_cords = chr(final_hor) + chr(final_ver)
    possible_cords.add(final_cords)

    # goes one place up and two places rigth
    final_ver = ord(vert_cord) + 1
    final_hor = ord(hori_cord) + 2
    final_cords = chr(final_hor) + chr(final_ver)
    possible_cords.add(final_cords)

    # goes two places down and one place left
    final_ver = ord(vert_cord) - 2
    final_hor = ord(hori_cord) - 1
    final_cords = chr(final_hor) + chr(final_ver)
    possible_cords.add(final_cords)

    # goes two places down and one place rigth
    final_ver = ord(vert_cord) - 2
    final_hor = ord(hori_cord) + 1
    final_cords = chr(final_hor) + chr(final_ver)
    possible_cords.add(final_cords)

    # goes one place down and two places left
    final_ver = ord(vert_cord) - 1
    final_hor = ord(hori_cord) - 2
    final_cords = chr(final_hor) + chr(final_ver)
    possible_cords.add(final_cords)

    # goes one place down and two places rigth
    final_ver = ord(vert_cord) - 1
    final_hor = ord(hori_cord) + 2
    final_cords = chr(final_hor) + chr(final_ver)
    possible_cords.add(final_cords)

    print(possible_cords)
    return possible_cords


class ChessBoard:
    def __init__(self) -> None:
        self.board = pd.DataFrame(
            {
                "a": ["*", "*", "*", "*", "*", "*", "*", "*"],
                "b": ["*", "*", "*", "*", "*", "*", "*", "*"],
                "c": ["*", "*", "*", "*", "*", "*", "*", "*"],
                "d": ["*", "*", "*", "*", "*", "*", "*", "*"],
                "e": ["*", "*", "*", "*", "*", "*", "*", "*"],
                "f": ["*", "*", "*", "*", "*", "*", "*", "*"],
                "g": ["*", "*", "*", "*", "*", "*", "*", "*"],
                "h": ["*", "*", "*", "*", "*", "*", "*", "*"],
            },
            index=[i + 1 for i in range(8)],
        )

    def stamp_moves(self, initial_pos, moves: list) -> None:
        self.board[initial_pos[0]][
            int(initial_pos[1])
        ] = "h"  # marking the horse start position
        for move in moves:
            self.board[move[0]][int(move[1])] = "o"

    # getter method
    def get_board(self) -> "board":
        return self.board


def main():
    initial_pos, final_pos = input().split()
    moves = all_moves(initial_pos)
    # places = all_moves()
    board = ChessBoard()
    board.stamp_moves(initial_pos, moves)
    marked_places = board.get_board()
    print(marked_places)


main()
