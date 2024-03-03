import random
import numpy as np
import threading
from backend import TSPSolver



SM = np.array([[0,13,27,18],
                [13,0,12,19],
                [27,12,0,14],
                [18,19,14,0]])

#====================================================


start_city = 0
solver = TSPSolver(SM, start_city)
solver.solve_tsp()
print("Best tour:", solver.best_tour)
print("Length of best tour:", solver.best_length)