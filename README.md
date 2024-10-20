
# Projects Overview

This repository contains two distinct projects: a **Maze Solver** and a **Phishing Detection Tool**. Each project demonstrates different applications of algorithms and machine learning techniques.

## Maze Solver

### Overview

The Maze Solver is an algorithmic tool that finds the shortest path through a maze using various search algorithms. This project illustrates the application of pathfinding algorithms like Depth-First Search (DFS) and Breadth-First Search (BFS).

### Features

- **Pathfinding Algorithms**: Implements DFS and BFS to navigate through the maze.
- **Visual Representation**: Provides a visual interface to display the maze and the solution path.
- **Custom Maze Input**: Users can input their own mazes for solving.

### Project Structure

```
maze_solver/
├── maze_solver.py         # Main script to run the maze solver
```

### Requirements

Make sure you have Python installed on your system. You may need the following package:

- `tkinter` (usually included with standard Python installations)

### Installation

1. Clone this repository or download the `maze_solver` folder.

### Usage

To run the maze solver, open your terminal or command prompt and navigate to the project directory. Then execute:

```bash
python maze_solver.py
```

### Instructions

1. Launch the application.
2. Input your maze (in the specified format) or load a sample maze.
3. Choose the desired algorithm (DFS or BFS) and click "Solve".
4. The solution path will be displayed visually.

---

## Phishing Detection Tool

### Overview

The Phishing Detection Tool identifies potential phishing websites by analyzing URL features. This application employs the K-Nearest Neighbors (KNN) algorithm and provides a user-friendly interface built with Tkinter.

### Features

- **Machine Learning Classification**: Uses the KNN algorithm to classify URLs as phishing or safe.
- **URL Feature Extraction**: Automatically extracts relevant features from input URLs.
- **User-Friendly GUI**: Developed with Tkinter for a seamless user experience.
- **Accuracy Display**: Shows the accuracy percentage of the trained model directly in the interface.

### Project Structure

```
phishing_detection/
├── phishing_data.csv        # Dataset used for training the model
└── phishing_detection_gui.py # Main script to run the phishing detection tool
```

### Requirements

Ensure you have Python installed on your system. You will also need the following packages:

- `pandas`
- `scikit-learn`
- `tkinter` (usually included with standard Python installations)

You can install the necessary packages via pip:

```bash
pip install pandas scikit-learn
```

### Installation

1. Clone this repository or download the `phishing_detection` folder.
2. Ensure the `phishing_data.csv` file is located in the same directory as `phishing_detection_gui.py`.

### Usage

To run the application, open your terminal or command prompt and navigate to the project directory. Then execute:

```bash
python phishing_detection_gui.py
```

### Instructions

1. Launch the application.
2. Enter a URL in the provided input field.
3. Click the "Check Phishing" button to evaluate the URL.
4. The tool will display whether the URL is safe or potentially phishing, along with the model's accuracy.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by various algorithmic studies and machine learning resources.
- Dataset used for phishing_detection: https://github.com/GregaVrbancic/Phishing-Dataset 
- Special thanks to the contributors and open-source community for their invaluable input.
