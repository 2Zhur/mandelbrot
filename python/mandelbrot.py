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
            2 * complex(real, imag) / img_size
            for real in range(-1 * (img_size // 2), (img_size // 2))
            for imag in range(-1 * (img_size // 2), (img_size // 2))
        ]
    ).reshape(img_shape)
    z_matrix = np.zeros(img_shape, dtype=complex)
    num_iterations = 10
    for i in range(num_iterations):
        z_matrix = mandelbrot_core_fn(z_matrix, c_matrix)
    print(z_matrix.shape)
    z_matrix_abs = np.absolute(z_matrix)
    max_val = np.nanmax(z_matrix_abs)
    z_norm = z_matrix_abs / max_val
    print(z_norm.shape)
    pixel_brightness = z_norm * 255
    pixel_brightness = pixel_brightness.astype('uint8')
    print(pixel_brightness)
    brightness_map = np.stack([pixel_brightness for _ in range(3)], axis=2)
    print(brightness_map.shape)
    img = Image.fromarray(brightness_map, "RGB")
    img.show("mandelbrot.png")
