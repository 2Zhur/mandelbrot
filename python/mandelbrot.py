from PIL import Image
import numpy as np


def mandelbrot_core_fn(z: complex, c: complex):
    return z * z + c


def get_pixel_brightness(c: complex, max_iterations: int) -> int:
    count = 0
    step_val = mandelbrot_core_fn(0, c)
    while (abs(step_val) > 1e-8) and (abs(step_val) < 2) and (count < max_iterations):
        step_val = mandelbrot_core_fn(step_val, c)
        count += 1
    if max_iterations >= count:
        return 255 - int(float(count * 255) / float(max_iterations))
    else:
        return 255


if __name__ == "__main__":
    square_img_size = 1024
    c_matrix = np.array(
        [
            complex(real, imag)
            for real in range(square_img_size)
            for imag in range(square_img_size)
        ]
    ).reshape((square_img_size, square_img_size))
    w, h = 1024, 1024
    max_iterations = 300
    t = (w, h, 3)
    A = np.full(t, 255, dtype=np.uint8)
    for i in range(-512, 512):
        for j in range(-512, 512):
            c = complex(float(i) / 256, float(j) / 256)
            tupl = tuple([get_pixel_brightness(c, max_iterations) for _ in range(3)])
            A[i + 512, j + 512] = tupl
            # A[i + 512, j + 512] = (255, 0, 0)
    img = Image.fromarray(A, "RGB")
    img.save("mandelbrot.png")
