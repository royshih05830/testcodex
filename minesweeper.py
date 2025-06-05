import random
from typing import List


class Cell:
    def __init__(self):
        self.mine = False
        self.adjacent = 0
        self.revealed = False
        self.flagged = False

class Minesweeper:
    def __init__(self, rows: int = 9, cols: int = 9, mines: int = 10):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board: List[List[Cell]] = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self._place_mines()
        self._calculate_adjacent()

    def _place_mines(self) -> None:
        positions = random.sample([(r, c) for r in range(self.rows) for c in range(self.cols)], self.mines)
        for r, c in positions:
            self.board[r][c].mine = True

    def _calculate_adjacent(self) -> None:
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c].mine:
                    continue
                count = 0
                for nr in range(max(0, r-1), min(self.rows, r+2)):
                    for nc in range(max(0, c-1), min(self.cols, c+2)):
                        if (nr != r or nc != c) and self.board[nr][nc].mine:
                            count += 1
                self.board[r][c].adjacent = count

    def reveal(self, r: int, c: int) -> bool:
        if not (0 <= r < self.rows and 0 <= c < self.cols):
            return True
        cell = self.board[r][c]
        if cell.revealed or cell.flagged:
            return True
        cell.revealed = True
        if cell.mine:
            return False
        if cell.adjacent == 0:
            for nr in range(max(0, r-1), min(self.rows, r+2)):
                for nc in range(max(0, c-1), min(self.cols, c+2)):
                    if nr != r or nc != c:
                        self.reveal(nr, nc)
        return True

    def toggle_flag(self, r: int, c: int) -> None:
        if not (0 <= r < self.rows and 0 <= c < self.cols):
            return
        cell = self.board[r][c]
        if not cell.revealed:
            cell.flagged = not cell.flagged

    def all_cleared(self) -> bool:
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.board[r][c]
                if not cell.mine and not cell.revealed:
                    return False
        return True

    def display(self) -> None:
        header = "   " + " ".join(str(i) for i in range(self.cols))
        print(header)
        for r in range(self.rows):
            row_display = []
            for c in range(self.cols):
                cell = self.board[r][c]
                if cell.revealed:
                    if cell.mine:
                        ch = '*'
                    elif cell.adjacent > 0:
                        ch = str(cell.adjacent)
                    else:
                        ch = ' '
                else:
                    ch = 'F' if cell.flagged else '.'
                row_display.append(ch)
            print(f"{r:2} " + " ".join(row_display))
    
    def  show_mesgage(self,msg):
        print(str(msg))


def main():
    game = Minesweeper()
    while True:
        game.display()
        cmd = input("Enter command (r row col: reveal, f row col: flag): ").strip().split()
        if len(cmd) != 3:
            print("Invalid command")
            continue
        action, r_str, c_str = cmd
        if not (r_str.isdigit() and c_str.isdigit()):
            print("Row and column must be numbers")
            continue
        r, c = int(r_str), int(c_str)
        if action.lower() == 'r':
            if not game.reveal(r, c):
                game.display()
                print("BOOM! You hit a mine.")
                break
            if game.all_cleared():
                game.display()
                print("Congratulations! You cleared the board.")
                break
        elif action.lower() == 'f':
            game.toggle_flag(r, c)
        else:
            print("Unknown action")


if __name__ == '__main__':
    main()
