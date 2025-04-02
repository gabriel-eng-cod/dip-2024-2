# image_geometry_exercise.py
# STUDENT'S EXERCISE FILE

"""
Exercise:
Implement a function `apply_geometric_transformations(img)` that receives a grayscale image
represented as a NumPy array (2D array) and returns a dictionary with the following transformations:

1. Translated image (shift right and down)
2. Rotated image (90 degrees clockwise)
3. Horizontally stretched image (scale width by 1.5)
4. Horizontally mirrored image (flip along vertical axis)
5. Barrel distorted image (simple distortion using a radial function)

You must use only NumPy to implement these transformations. Do NOT use OpenCV, PIL, skimage or similar libraries.

Function signature:
    def apply_geometric_transformations(img: np.ndarray) -> dict:

The return value should be like:
{
    "translated": np.ndarray,
    "rotated": np.ndarray,
    "stretched": np.ndarray,
    "mirrored": np.ndarray,
    "distorted": np.ndarray
}
"""

import numpy as np
import matplotlib.pyplot as plt

def translate_image(img: np.ndarray, shift_x: int, shift_y: int) -> np.ndarray:
    """Translated image (shift right and down) - Desloca a imagem para a direita e para baixo."""
    h, w = img.shape
    translated = np.zeros_like(img)
    translated[shift_y:h, shift_x:w] = img[0:h-shift_y, 0:w-shift_x]
    return translated

def rotate_image(img: np.ndarray) -> np.ndarray:
    """Rotated image (90 degrees clockwise) - Rotaciona a imagem 90 graus no sentido horário."""
    return np.rot90(img, k=-1)

def stretch_image(img: np.ndarray, scale_x: float) -> np.ndarray:
    """Horizontally stretched image (scale width by 1.5) - Estica a imagem horizontalmente por um fator de scale_x."""
    h, w = img.shape
    new_w = int(w * scale_x)
    stretched = np.zeros((h, new_w))
    x_indices = (np.linspace(0, w-1, new_w)).astype(int)
    stretched[:, :] = img[:, x_indices]
    return stretched

def mirror_image(img: np.ndarray) -> np.ndarray:
    """Horizontally mirrored image (flip along vertical axis) - Espelha a imagem horizontalmente."""
    return img[:, ::-1]

def barrel_distort_image(img: np.ndarray) -> np.ndarray:
    """Barrel distorted image (simple distortion using a radial function) - Aplica uma distorção de barril simples usando uma função radial."""
    h, w = img.shape
    distorted = np.zeros_like(img)
    center_x, center_y = w // 2, h // 2
    
    for i in range(h):
        for j in range(w):
            dx = (j - center_x) / w
            dy = (i - center_y) / h
            r = np.sqrt(dx**2 + dy**2)
            factor = 1 + 0.5 * (r ** 2)
            src_x = int(center_x + (j - center_x) / factor)
            src_y = int(center_y + (i - center_y) / factor)
            
            if 0 <= src_x < w and 0 <= src_y < h:
                distorted[i, j] = img[src_y, src_x]
    
    return distorted

def apply_geometric_transformations(img: np.ndarray) -> dict:
    """Aplica transformações geométricas em uma imagem e retorna um dicionário com os resultados."""
    return {
        "translated": translate_image(img, shift_x=10, shift_y=10),
        "rotated": rotate_image(img),
        "stretched": stretch_image(img, scale_x=1.5),
        "mirrored": mirror_image(img),
        "distorted": barrel_distort_image(img)
    }

if __name__ == "__main__":
    # Criando uma imagem de exemplo (quadrado branco no fundo preto)
    img = np.zeros((100, 100))
    img[30:70, 30:70] = 1

    results = apply_geometric_transformations(img)

    fig, axes = plt.subplots(1, 6, figsize=(15, 5))
    titles = ["Original", "Translated", "Rotated", "Stretched", "Mirrored", "Distorted"]
    
    axes[0].imshow(img, cmap="gray")
    axes[0].set_title("Original")

    for ax, (key, transformed_img) in zip(axes[1:], results.items()):
        ax.imshow(transformed_img, cmap="gray")
        ax.set_title(key.capitalize())

    for ax in axes:
        ax.axis("off")

    plt.show()