
"""
Version 1:
update this code
1. Display Question
2. Change format of board

Version 2 
1. Creates a random sudoku puzzle 
2. Gives the user 5 mins to solve it
3. Displays Answer
"""

from threading import main_thread
from tkinter import E
from tkinter.tix import MAIN
from pip import main
import time
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
        sudoku.print_question(problem)
    elif difficulty == "M":
        problem = medium_grid
        sudoku.print_question(problem)
    elif difficulty == "H":
        problem = hard_grid
        sudoku.print_question(problem)
    
    print(end = "\n\n")
    print("You have 2 minutes to solve this! Good luck.", end = '\n')
    time.sleep(120)
    print("Time's up!", end = '\n')
    time.sleep(3)
    print("Check your answer.", end = '\n\n')

    if sudoku.solve_sudoku(problem,0,0):
        sudoku.print_solution(problem)
    else:
        print("Invalid")
