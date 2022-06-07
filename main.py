from threading import main_thread
from tkinter import E
from tkinter.tix import MAIN
from pip import main
import sudoku

easy_grid = [[0, 7, 0, 0, 2, 0, 0, 4, 6],
             [0, 6, 0, 0, 0, 0, 8, 9, 0],
             [2, 0, 0, 8, 0, 0, 7, 1, 5],
             [0, 8, 4, 0, 9, 7, 0, 0, 0],
             [7, 1, 0, 0, 0, 0, 0, 5, 9],
             [0, 0, 0, 1, 3, 0, 4, 8, 0],
             [6, 9, 7, 0, 0, 2, 0, 0, 8],
             [0, 5, 8, 0, 0, 0, 0, 6, 0],
             [4, 3, 0, 0, 8, 0, 0, 7, 0]]

medium_grid =  [[5, 0, 7, 2, 0, 0, 0, 9, 0],
                [0, 0, 6, 0, 3, 0, 7, 0, 1],
                [4, 0, 0, 0, 0, 0, 0, 6, 0],
                [1, 0, 0, 4, 9, 0, 0, 0, 7],
                [0, 0, 0, 5, 0, 8, 0, 0, 0],
                [8, 0, 0, 0, 2, 7, 0, 0, 5],
                [0, 7, 0, 0, 0, 0, 0, 0, 9],
                [2, 0, 9, 0, 8, 0, 6, 0, 0],
                [0, 4, 0, 0, 0, 9, 3, 0, 8]]

hard_grid = [[2, 0, 0, 5, 0, 7, 4, 0, 6],
             [0, 0, 0, 0, 3, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 2, 3, 0],
             [0, 0, 0, 0, 2, 0, 0, 0, 0],
             [8, 6, 0, 3, 1, 0, 0, 0, 0],
             [0, 4, 5, 0, 0, 0, 0, 0, 0],
             [0, 0, 9, 0, 0, 0, 7, 0, 0],
             [0, 0, 6, 9, 5, 0, 0, 0, 2],
             [0, 0, 1, 0, 0, 6, 0, 0, 8]]

if __name__ == '__main__':
    #Solve Sudoku
    print("Hello! Let's play a game of Sudoku.", end ='\n')
    print("Choose your difficulty by entering one of the following:", end = '\n\t')
    print ("E : Easy", end = '\n\t')
    print ("M : Medium", end = '\n\t')
    print ("E : Hard", end = '\n')
    difficulty = input ("Enter Difficulty Level: ")
    print (end = '\n')

    if difficulty == "E":
        problem = easy_grid
    elif difficulty == "M":
        problem = medium_grid
    elif difficulty == "H":
        problem = hard_grid
    
    if sudoku.solve_sudoku(problem,0,0):
        sudoku.print_solution(problem)
    else:
        print("Invalid")
