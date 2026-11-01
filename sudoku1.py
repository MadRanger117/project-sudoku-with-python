import sys
from clingo.application import Application, clingo_main

class ClingoApp(Application):
    def __init__(self, name):
        self.program_name = name
    def main(self, control, files):
        control.load("sudoku.lp")
        for file in files:
            control.load(file)
        control.ground([("base", [])])
        control.solve()
        
    def print_model(self, model, printer):
        symbols = model.symbols(shown=True)
        print(model.number)
        print("".join(str(symbol) for symbol in sorted(symbols, key=str)))
        
if __name__ == "__main__":
    clingo_main(ClingoApp("sudoku1"), sys.argv[1:])
    
