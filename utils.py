import numpy as np

def rotate_4d(point, angle, axis):
    """
    Rotate a 4D point about a specified axis by a given angle.
    """
    # Normalize the rotation axis
    axis = axis / np.linalg.norm(axis)

    # Compute the rotation matrix
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)
    x, y, z, w = axis

    rotation_matrix = np.array([
        [cos_theta + x**2 * (1 - cos_theta), x * y * (1 - cos_theta) - z * sin_theta, x * z * (1 - cos_theta) + y * sin_theta, x * w * (1 - cos_theta)],
        [y * x * (1 - cos_theta) + z * sin_theta, cos_theta + y**2 * (1 - cos_theta), y * z * (1 - cos_theta) - x * sin_theta, y * w * (1 - cos_theta)],
        [z * x * (1 - cos_theta) - y * sin_theta, z * y * (1 - cos_theta) + x * sin_theta, cos_theta + z**2 * (1 - cos_theta), z * w * (1 - cos_theta)],
        [w * x * (1 - cos_theta), w * y * (1 - cos_theta), w * z * (1 - cos_theta), cos_theta + w**2 * (1 - cos_theta)]
    ])

    # Apply the rotation matrix to the point
    rotated_point = np.dot(rotation_matrix, point)

    return rotated_point