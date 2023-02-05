from PIL import Image
import numpy as np


def mandelbrot_core_fn(z, c):
    return z * z + c


def get_pixel_values(z_mtrx):

    return


if __name__ == "__main__":
    img_size = 1024
    img_shape = (img_size, img_size)
    c_matrix = np.array(
        [
            complex(real, imag) / (2 * img_size)
            for real in range(-1 * (img_size / 2), (img_size / 2))
            for imag in range(-1 * (img_size / 2), (img_size / 2))
        ]
    ).reshape(img_shape)
    z_matrix = np.zeros(img_shape)
    num_iterations = 10
    for i in range(num_iterations):
        z_matrix = mandelbrot_core_fn(z_matrix, c_matrix)
    max_val = np.nanmax(z_matrix)
    z_matrix = np.where(np.isfinite(z_matrix), z_matrix, max_val)

    img_array_shape = (*z_matrix.shape, 3)
    z_matrix_normalized = z_matrix / max_val
    img_array = np.array([np.full(3, np.uint8(255.0 * val)) for val in z_matrix_normalized.flatten()]).reshape(img_array_shape)
    img = Image.fromarray(img_array, "RGB")
    img.save("mandelbrot.png")
