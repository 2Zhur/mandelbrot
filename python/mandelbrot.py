from PIL import Image
from copy import deepcopy

# from scipy.special import expit
import numpy as np

# the entire set is inside a circle with r=2, i.e. r**2=4
MAX_DISTANCE = 2
MAX_SQR = MAX_DISTANCE**2


def mandelbrot_core_fn(z, c):
    return z * z + c


def main():
    img_size = 4096
    img_half_size = img_size // 2
    assert img_half_size * 2 == img_size, "Please use even image size!"

    imags = [
        2 * float(x_pixels) / float(img_half_size)
        for x_pixels in range(-1 * img_half_size, img_half_size)
    ]
    reals = deepcopy(imags)
    imags.reverse()
    img_shape = (img_size, img_size)
    c_mtrx = np.array([complex(r, i) for r in reals for i in imags])
    c_mtrx = c_mtrx.reshape(img_shape)
    z_mtrx = np.zeros(img_shape)
    # a matrix to count how many steps it took to exceed 2 on any axis
    step_count_mtrx = np.zeros(img_shape, dtype=int)
    ones_mtrx = np.ones(img_shape, dtype=int)
    zeros_mtrx = np.zeros(img_shape, dtype=int)

    max_iterations = 1000
    for _ in range(max_iterations):
        z_mtrx = mandelbrot_core_fn(z_mtrx, c_mtrx)
        step_count_mtrx += np.where(
            np.absolute(z_mtrx) < MAX_DISTANCE, ones_mtrx, zeros_mtrx
        )

    # create a 'trajectory' through RGB space
    rgb_gradient = np.array(
        [(i, 0, 0) for i in range(256)]
        + [(255, i, 0) for i in range(1, 256)]
        + [(255, 255, i) for i in range(1, 256)]
        + [(i, 255, 255) for i in range(255, 0, -1)]
        + [(0, i, 255) for i in range(255, 0, -1)]
        + [(0, 0, i) for i in range(255, 50, -1)],
    ).astype(dtype=np.int8)
    num_colors = len(rgb_gradient)

    scale = float(num_colors) / float(max_iterations)

    color_map = np.rint(step_count_mtrx * scale).astype(dtype=int).flatten()

    
    img_arr = [rgb_gradient[idx if idx < num_colors else num_colors - 1] for idx in color_map]
    img_arr = np.array(img_arr).reshape((*img_shape, 3))

    img = Image.fromarray(img_arr, "RGB")
    img.save("mandelbrot.png")


if __name__ == "__main__":
    main()
