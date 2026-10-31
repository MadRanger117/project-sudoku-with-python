import sys
from clingo.application import Application, clingo_main

class ClingoApp(Application):
    def __init__(self, name):
        self.program_name = name
    def main(self, control, files):
        control.load("sudoku.lp")
        control.load(files)
        control.ground([("base", [])])
        control.solve()
        
    # def print_alphabetical(filename):
    #   with open(filename, 'r') as file:
    #     lines = file.readlines()
    #   lines.sort()
    #   with open(filename, 'w') as file:
    #     file.writelines(lines)

    
