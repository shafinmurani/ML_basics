import turtle
import random
import heapq
import tkinter as tk
from tkinter import messagebox, ttk

# Define the grid size
grid_size = 21  # Maze needs to be an odd number for walls and paths to align properly

# Create a turtle to draw the maze
maze_turtle = turtle.Turtle()
maze_turtle.speed(0)  # Set the speed to the fastest
maze_turtle.shape("square")
maze_turtle.penup()
maze_turtle.hideturtle()

# Create a turtle to visualize the explored paths
explorer_turtle = turtle.Turtle()
explorer_turtle.shape("square")
explorer_turtle.color("yellow")
explorer_turtle.penup()
explorer_turtle.speed(0)

# Create a turtle to visualize the final path
solver_turtle = turtle.Turtle()
solver_turtle.shape("square")
solver_turtle.color("blue")
solver_turtle.penup()
solver_turtle.speed(0)

# The maze grid (1 = wall, 0 = open space)
maze = [[1 for _ in range(grid_size)] for _ in range(grid_size)]

# Directions for maze generation and solving
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

# Statistics
stats = {
    'nodes_explored': 0,
    'steps_to_goal': 0  # New stat for steps to goal
}

def draw_square(x, y, color):
    """Draws a square at the given x, y position."""
    maze_turtle.goto(x * 24 - 300, 300 - y * 24)
    maze_turtle.color(color)
    maze_turtle.stamp()

def generate_maze(x, y):
    """Generates a random maze using depth-first search."""
    maze[x][y] = 0  # Mark the current cell as a path
    draw_square(x, y, "white")  # Draw the current path as white

    directions_shuffled = directions[:]
    random.shuffle(directions_shuffled)

    for dx, dy in directions_shuffled:
        nx, ny = x + dx * 2, y + dy * 2  # Move two steps in the current direction
        if 0 <= nx < grid_size and 0 <= ny < grid_size and maze[nx][ny] == 1:
            # Remove the wall between the current cell and the next
            maze[x + dx][y + dy] = 0
            draw_square(x + dx, y + dy, "white")  # Draw the path
            generate_maze(nx, ny)

def heuristic(a, b):
    """Heuristic function for Greedy Best-First Search (Manhattan distance)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy_best_first_search(start, goal):
    """Greedy Best-First Search algorithm to solve the maze."""
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), start))  # (estimated cost, node)
    came_from = {}
    explored = set()

    while pq:
        current = heapq.heappop(pq)[1]
        if current == goal:
            return reconstruct_path(came_from, current)

        if current not in explored:
            visualize_explored_path(current)
            explored.add(current)
            stats['nodes_explored'] += 1  # Increment nodes explored

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size:
                if maze[neighbor[0]][neighbor[1]] == 1:
                    continue  # Wall

                if neighbor not in explored:
                    came_from[neighbor] = current
                    heapq.heappush(pq, (heuristic(neighbor, goal), neighbor))

    return None

def bfs(start, goal):
    """Breadth-First Search algorithm to solve the maze."""
    queue = [start]
    came_from = {}
    explored = set()

    while queue:
        current = queue.pop(0)

        if current == goal:
            return reconstruct_path(came_from, current)

        if current not in explored:
            visualize_explored_path(current)
            explored.add(current)
            stats['nodes_explored'] += 1  # Increment nodes explored

            for dx, dy in directions:
                neighbor = (current[0] + dx, current[1] + dy)
                if 0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size:
                    if maze[neighbor[0]][neighbor[1]] == 1:
                        continue  # Wall

                    if neighbor not in explored and neighbor not in queue:
                        came_from[neighbor] = current
                        queue.append(neighbor)

    return None

def dfs(start, goal):
    """Depth-First Search algorithm to solve the maze."""
    stack = [start]
    came_from = {}
    explored = set()

    while stack:
        current = stack.pop()

        if current == goal:
            return reconstruct_path(came_from, current)

        if current not in explored:
            visualize_explored_path(current)
            explored.add(current)
            stats['nodes_explored'] += 1  # Increment nodes explored

            for dx, dy in directions:
                neighbor = (current[0] + dx, current[1] + dy)
                if 0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size:
                    if maze[neighbor[0]][neighbor[1]] == 1:
                        continue  # Wall

                    if neighbor not in explored:
                        came_from[neighbor] = current
                        stack.append(neighbor)

    return None

def reconstruct_path(came_from, current):
    """Reconstruct the path from start to goal."""
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    stats['steps_to_goal'] = len(total_path) - 1  # Update steps to goal (subtract 1 for starting point)
    return total_path

def visualize_explored_path(position):
    """Visualize the paths explored by the search algorithms."""
    x, y = position
    explorer_turtle.goto(x * 24 - 300, 300 - y * 24)
    explorer_turtle.stamp()

def visualize_path(path):
    """Visualize the final path found by the search algorithms using Turtle."""
    for x, y in path:
        solver_turtle.goto(x * 24 - 300, 300 - y * 24)
        solver_turtle.stamp()

def draw_maze():
    """Draws the maze with walls and paths."""
    for i in range(grid_size):
        for j in range(grid_size):
            if maze[i][j] == 1:
                # Draw walls in black
                maze_turtle.goto(i * 24 - 300, 300 - j * 24)
                maze_turtle.color("black")
                maze_turtle.stamp()

def label_start_end(start, goal):
    """Labels the start and end positions."""
    maze_turtle.goto(start[0] * 24 - 300, 300 - start[1] * 24)
    maze_turtle.color("red")  # Change font color to red
    maze_turtle.write("A", align="center", font=("Arial", 16, "bold"))
    
    maze_turtle.goto(goal[0] * 24 - 300, 300 - goal[1] * 24)
    maze_turtle.color("red")  # Change font color to red
    maze_turtle.write("B", align="center", font=("Arial", 16, "bold"))

def run_algorithm(selected_algorithm):
    """Runs the selected algorithm to solve the maze."""
    start = (1, 1)
    goal = (grid_size - 2, grid_size - 2)
    
    # Generate random maze
    generate_maze(start[0], start[1])
    
    # Draw the maze walls
    draw_maze()
    
    # Mark start and goal
    draw_square(start[0], start[1], "green")  # Start as green
    draw_square(goal[0], goal[1], "red")      # Goal as red
    
    # Label the start and end positions
    label_start_end(start, goal)
    
    # Reset statistics
    stats['nodes_explored'] = 0  # Reset nodes explored
    stats['steps_to_goal'] = 0    # Reset steps to goal
    
    # Run the selected algorithm and visualize the solution
    if selected_algorithm == "Greedy Best-First Search":
        path = greedy_best_first_search(start, goal)
    elif selected_algorithm == "Breadth-First Search":
        path = bfs(start, goal)
    elif selected_algorithm == "Depth-First Search":
        path = dfs(start, goal)
    else:
        return

    if path is not None:
        visualize_path(path)
        show_statistics()
    else:
        messagebox.showinfo("Result", "No path found.")

def show_statistics():
    """Display the statistics in a separate Tkinter window."""
    stats_window = tk.Tk()
    stats_window.title("Maze Solver Statistics")

    # Create labels for statistics
    ttk.Label(stats_window, text=f"Nodes Explored: {stats['nodes_explored']}").pack()
    ttk.Label(stats_window, text=f"Steps to Goal: {stats['steps_to_goal']}").pack()

    # Start the Tkinter main loop
    stats_window.mainloop()

# Main GUI setup
def setup_gui():
    root = tk.Tk()
    root.title("Maze Solver")
    
    algorithm_label = ttk.Label(root, text="Choose Algorithm:")
    algorithm_label.pack()

    algorithms = ["Greedy Best-First Search", "Breadth-First Search", "Depth-First Search"]
    selected_algorithm = tk.StringVar()
    selected_algorithm.set(algorithms[0])  # Default value

    algorithm_menu = ttk.OptionMenu(root, selected_algorithm, *algorithms)
    algorithm_menu.pack()

    run_button = ttk.Button(root, text="Run Algorithm", command=lambda: run_algorithm(selected_algorithm.get()))
    run_button.pack()

    turtle.mainloop()

# Start the GUI
setup_gui()
