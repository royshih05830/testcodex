# testcodex

This repository contains a simple command-line Minesweeper game written in Python.

## How to run

Execute the script using Python 3. You can optionally specify the board size and
number of mines:

```
python minesweeper.py [--rows N] [--cols N] [--mines N]
```

For example, to play on a 12×10 board with 20 mines:

```
python minesweeper.py --rows 12 --cols 10 --mines 20
```

During the game use the following commands:

- `r row col` – reveal the cell at `row`, `col`.
- `f row col` – toggle a flag on the cell at `row`, `col`.

Rows and columns are zero-indexed.
