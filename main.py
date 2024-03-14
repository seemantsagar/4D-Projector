import sys
import traceback
from objects import Cube
from visualization import plot_4d_projection

def main():
    try:
        # Create a 3D object (e.g., a Cube)
        cube = Cube(size=2)

        # Get the 4D projection of the 3D object
        projection = cube.get_4d_projection()

        # Plot the 4D projection in a 3D plane
        plot_4d_projection(projection)

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc(file=sys.stderr)

if __name__ == "__main__":
    main()