import math
import random
import numpy as np


def lerp(a, b, w):
    return a + w * (b - a)


def smoothstep(x):
    return 3 * x**2 - 2 * x**3


def get_chunk_dimensions(matrix):
    """return number of chunks in a matrix
    value in returned as amount of rows and columns of chunks"""
    rows = len(matrix)
    cols = len(matrix[0])
    return rows - 1, cols - 1


def calc_pixel_value(matrix, chunk_size, pixel_x, pixel_y):
    lerp_weigh_x = (pixel_x % chunk_size + 0.5) / chunk_size
    lerp_weigh_y = (pixel_y % chunk_size + 0.5) / chunk_size

    col = math.floor(pixel_x / chunk_size)
    row = math.floor(pixel_y / chunk_size)

    # Get corner vectors
    # A---B
    # |   |
    # C---D
    a_vec = matrix[row][col]
    b_vec = matrix[row][col + 1]
    c_vec = matrix[row + 1][col]
    d_vec = matrix[row + 1][col + 1]
    
    # calc vectors from corners to point
    a_to_point_vec = np.array([lerp_weigh_x,lerp_weigh_y])
    b_to_point_vec = np.array([lerp_weigh_x-1,lerp_weigh_y])
    c_to_point_vec = np.array([lerp_weigh_x,lerp_weigh_y-1])
    d_to_point_vec = np.array([lerp_weigh_x-1,lerp_weigh_y-1])


    ab_vec = lerp(np.dot(a_vec,a_to_point_vec),np.dot(b_vec, b_to_point_vec), smoothstep(lerp_weigh_x))
    cd_vec = lerp(np.dot(c_vec, c_to_point_vec), np.dot(d_vec, d_to_point_vec), smoothstep(lerp_weigh_x))
    out_vec = lerp(ab_vec, cd_vec, smoothstep(lerp_weigh_y))
    out_vec = (out_vec + 1)/2
    return math.floor(out_vec * 255)


def generate_perlin(matrix: list, chunk_size: int):
    rows, cols = get_chunk_dimensions(matrix)
    image_width = cols * chunk_size
    image_height = rows * chunk_size

    with open("out.pgm", "w") as file:
        file.write(f"P2\n{image_width} {image_height}\n255\n")
        for y in range(image_height):
            file.write(
                " ".join(
                    str(calc_pixel_value(matrix, chunk_size, x, y))
                    for x in range(image_width)
                )
            )
            file.write("\n")
    
def generate_random_vector():
    # original Perlin algorithm for random vector with nonequal distribution
    return np.array([random.random() * 2 - 1, random.random() * 2 - 1])


def generate_vector_grid(chunks_x, chunks_y):
    """Create matrix of random vectors
    matrix size is determined by chunk_size + 1"""

    matrix = []
    for _ in range(chunks_y + 1):
        row = []
        for _ in range(chunks_x + 1):
            row.append(generate_random_vector())
        matrix.append(row)

    return matrix


if __name__ == "__main__":
    matrix = generate_vector_grid(20, 10)
    generate_perlin(matrix, 20)
