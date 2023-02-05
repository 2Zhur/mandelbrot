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
    bool_mtrx = np.isfinite(z_matrix)

    img_array_shape = (*z_matrix.shape, 3)
    max_val = np.nanmax(z_matrix)
    z_matrix_normalized = z_matrix / max_val

    w, h = 1024, 1024
    max_iterations = 300
    t = (w, h, 3)
    A = np.full(t, 255, dtype=np.uint8)
    for i in range(-512, 512):
        for j in range(-512, 512):
            c = complex(float(i) / 256, float(j) / 256)
            tupl = tuple([get_pixel_values(c, max_iterations) for _ in range(3)])
            A[i + 512, j + 512] = tupl
            # A[i + 512, j + 512] = (255, 0, 0)
    img = Image.fromarray(A, "RGB")
    img.save("mandelbrot.png")
