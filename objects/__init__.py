import numpy as np
from utils import rotate_4d

class Cube:
    def __init__(self, size=1):
        self.size = size
        self.vertices = self.generate_vertices()

    def generate_vertices(self):
        """
        Generate the 4D vertices of the cube.
        """
        vertices = []
        for x in [-self.size, self.size]:
            for y in [-self.size, self.size]:
                for z in [-self.size, self.size]:
                    for w in [-self.size, self.size]:
                        vertices.append(np.array([x, y, z, w]))
        return np.array(vertices)

    def get_4d_projection(self):
        """
        Get the 4D projection of the cube in a 3D plane.
        """
        # Rotate the 4D vertices to get the desired projection
        rotation_angle = np.pi / 4  # Rotate by 45 degrees
        rotation_axis = np.array([1, 1, 1, 1])  # Rotate about the (1, 1, 1, 1) axis
        rotated_vertices = [rotate_4d(vertex, rotation_angle, rotation_axis) for vertex in self.vertices]

        # Project the rotated 4D vertices onto the (x, y, z) 3D plane
        projection = np.array([vertex[:3] for vertex in rotated_vertices])

        return projection