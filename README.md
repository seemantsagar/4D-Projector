# 4D Projection of 3D Objects

This project provides a Python implementation to create a 4D projection of a 3D object in a 3D plane. It utilizes the Matplotlib and Plotly libraries for visualization.

## Project Structure

The project is organized as follows:

project_4d/
├── README.md
├── main.py
├── utils.py
├── visualization.py
└── objects/
├── init.py
└── cube.py

- `main.py`: Entry point of the application.
- `utils.py`: Contains utility functions for 4D rotations.
- `visualization.py`: Contains functions for plotting the 4D projection.
- `objects/`: Package containing classes for 3D objects.
  - `__init__.py`: Initializes the package.
  - `cube.py`: Implements the Cube class.

## Getting Started

1. Clone the repository
2. Navigate to the project directory
3. Install the required dependencies
4. Run the application

This will create a Cube object, obtain its 4D projection, and plot the projection in a 3D plane using Matplotlib and Plotly.

## Usage

The `main.py` file is the entry point of the application. It creates a 3D object (in this case, a Cube), obtains its 4D projection, and plots the projection in a 3D plane using the provided visualization functions.

You can modify the `main.py` file to create different 3D objects or adjust the visualization parameters as needed.
