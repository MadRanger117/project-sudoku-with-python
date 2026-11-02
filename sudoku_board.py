from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        for row in range(1, 10):
            if row == 4 or row == 7:
                s += "\n"
            for col in range(1,10):
                if col == 4 or col == 7:
                    s += "  "
                else:
                    s += " "
                s += str(self.sudoku[(row, col)])
            s += "\n"
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        nums = s.split()
        index = 0
        for row in range(1, 10):
            for col in range(1,10):
                sudoku[(row, col)] = int(nums[index])
                index += 1
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        for symbol in model.symbols(shown=True):
            arguments = symbol.arguments
            row = arguments[0].number
            col = arguments[1].number
            val = arguments[2].number
            sudoku[(row, col)] = val
        return cls(sudoku)
