import argparse
import tkinter as tk
from tkinter import messagebox

from minesweeper import Minesweeper


class MinesweeperGUI:
    def __init__(self, rows: int, cols: int, mines: int) -> None:
        self.game = Minesweeper(rows, cols, mines)
        self.rows = rows
        self.cols = cols
        self.root = tk.Tk()
        self.root.title("Minesweeper")
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self._create_buttons()

    def _create_buttons(self) -> None:
        for r in range(self.rows):
            for c in range(self.cols):
                btn = tk.Button(
                    self.root,
                    width=2,
                    height=1,
                    command=lambda r=r, c=c: self.on_left_click(r, c),
                )
                btn.bind("<Button-3>", lambda e, r=r, c=c: self.on_right_click(r, c))
                btn.grid(row=r, column=c)
                self.buttons[r][c] = btn

    def on_left_click(self, r: int, c: int) -> None:
        if not self.game.reveal(r, c):
            self.update_buttons()
            messagebox.showinfo("Game Over", "BOOM! You hit a mine.")
            self.disable_buttons()
            return
        self.update_buttons()
        if self.game.all_cleared():
            messagebox.showinfo("You win", "Congratulations! You cleared the board.")
            self.disable_buttons()

    def on_right_click(self, r: int, c: int) -> None:
        self.game.toggle_flag(r, c)
        self.update_buttons()

    def update_buttons(self) -> None:
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.game.board[r][c]
                btn = self.buttons[r][c]
                if cell.revealed:
                    btn.config(relief=tk.SUNKEN, state=tk.DISABLED)
                    if cell.mine:
                        btn.config(text="*")
                    elif cell.adjacent > 0:
                        btn.config(text=str(cell.adjacent))
                    else:
                        btn.config(text=" ")
                else:
                    btn.config(text="F" if cell.flagged else "", state=tk.NORMAL, relief=tk.RAISED)

    def disable_buttons(self) -> None:
        for row in self.buttons:
            for btn in row:
                btn.config(state=tk.DISABLED)

    def run(self) -> None:
        self.root.mainloop()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Minesweeper GUI")
    parser.add_argument("--rows", type=int, default=9, help="Number of rows")
    parser.add_argument("--cols", type=int, default=9, help="Number of columns")
    parser.add_argument("--mines", type=int, default=10, help="Number of mines")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    gui = MinesweeperGUI(args.rows, args.cols, args.mines)
    gui.run()


if __name__ == "__main__":
    main()
