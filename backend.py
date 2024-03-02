import numpy as np
import threading

class TSPSolver:
    def __init__(self, distances, start_city):
        self.distances = distances
        self.num_cities = len(distances)
        self.num_threads = min(self.num_cities, 4)  # Limiting threads for illustration
        self.start_city = start_city

    def solve_tsp(self):
        self.best_tour = None
        self.best_length = float('inf')
        self.lock = threading.Lock()

        for start_city in range(self.num_cities):
            thread = threading.Thread(target=self.solve_tsp_from_start)
            thread.start()

    def solve_tsp_from_start(self):
        visited = [False] * self.num_cities
        tour = [self.start_city]
        visited[self.start_city] = True
        self.tsp_recursive(1, self.start_city, tour, visited)

    def tsp_recursive(self, depth, current_city, tour, visited):
        if depth == self.num_cities:
            length = self.calculate_tour_length(tour)
            with self.lock:
                if length < self.best_length:
                    self.best_length = length
                    self.best_tour = tour.copy()
            return

        for next_city in range(self.num_cities):
            if not visited[next_city]:
                visited[next_city] = True
                tour.append(next_city)
                self.tsp_recursive(depth + 1, next_city, tour, visited)
                tour.pop()
                visited[next_city] = False

    def calculate_tour_length(self, tour):
        length = 0
        for i in range(self.num_cities - 1):
            length += self.distances[tour[i]][tour[i + 1]]
        length += self.distances[tour[-1]][tour[0]]
        return length
if __name__=="__main__":
    # Example usage:
    # Define the distances between cities (example distances)
    distances = np.array([[0, 5, 6, 15],
                        [5, 0, 8, 3],
                        [6, 8, 0, 12],
                        [15, 3, 12, 0]])
    #numpy_array = np.random.rand(10, 10)*100
    #np.fill_diagonal(numpy_array, 0)

    solver = TSPSolver(distances)
    solver.solve_tsp()
    print("Best tour:", solver.best_tour)
    print("Length of best tour:", solver.best_length)
