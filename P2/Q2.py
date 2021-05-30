import pandas as pd

"talvez usar pd na criacao de um objeto chess table"


def all_moves(position: str) -> str:
    hori_coord = position[
        0
    ]  # represents the letter in the position (horizontal coordinate)
    vert_coord = position[
        1
    ]  # represents the number in the position (vertical coordinate)
    possible_coords = []

    # goes two places up and one place left
    final_vert = ord(vert_coord) + 2
    final_hori = ord(hori_coord) - 1
    final_cords = chr(final_hori) + chr(final_vert)
    possible_coords.append(final_cords)

    # goes two places up and one place rigth
    final_vert = ord(vert_coord) + 2
    final_hori = ord(hori_coord) + 1
    final_cords = chr(final_hori) + chr(final_vert)
    possible_coords.append(final_cords)

    # goes one place up and two places left
    final_vert = ord(vert_coord) + 1
    final_hori = ord(hori_coord) - 2
    final_cords = chr(final_hori) + chr(final_vert)
    possible_coords.append(final_cords)

    # goes one place up and two places rigth
    final_vert = ord(vert_coord) + 1
    final_hori = ord(hori_coord) + 2
    final_cords = chr(final_hori) + chr(final_vert)
    possible_coords.append(final_cords)

    # goes two places down and one place left
    final_vert = ord(vert_coord) - 2
    final_hori = ord(hori_coord) - 1
    final_cords = chr(final_hori) + chr(final_vert)
    possible_coords.append(final_cords)

    # goes two places down and one place rigth
    final_vert = ord(vert_coord) - 2
    final_hori = ord(hori_coord) + 1
    final_cords = chr(final_hori) + chr(final_vert)
    possible_coords.append(final_cords)

    # goes one place down and two places left
    final_vert = ord(vert_coord) - 1
    final_hori = ord(hori_coord) - 2
    final_cords = chr(final_hori) + chr(final_vert)
    possible_coords.append(final_cords)

    # goes one place down and two places rigth
    final_vert = ord(vert_coord) - 1
    final_hori = ord(hori_coord) + 2
    final_cords = chr(final_hori) + chr(final_vert)
    possible_coords.append(final_cords)

    print(possible_coords)
    return possible_coords


def possible_moves(possible_coords: list) -> list:
    possible_moves = []
    for coordinates in possible_coords:
        hori_coord = coordinates[0]
        verti_coord = coordinates[1]
        if (
            ord(hori_coord) > 104 or ord(hori_coord) < 97
        ):  # whether the horse has crossed the left or right limit
            print(f"Ops limit transpassed: {hori_coord}")
            continue
        elif (
            ord(verti_coord) > 56 or ord(verti_coord) < 49
        ):  # whether the horse has crossed the upper or loewr limit
            print(f"Ops limit transpassed: {verti_coord}")
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
    valid_moves = possible_moves(moves)
    # creating the chess board, stamping the moves on it and printing this board
    board = ChessBoard()
    board.stamp_moves(initial_pos, valid_moves)
    marked_places = board.get_board()
    print(marked_places)


main()
