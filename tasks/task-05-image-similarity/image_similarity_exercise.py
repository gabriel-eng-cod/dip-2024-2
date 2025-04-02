# image_similarity_exercise.py
# STUDENT'S EXERCISE FILE

"""
Exercise:
Implement a function `compare_images(i1, i2)` that receives two grayscale images
represented as NumPy arrays (2D arrays of shape (H, W)) and returns a dictionary with the following metrics:

1. Mean Squared Error (MSE)
2. Peak Signal-to-Noise Ratio (PSNR)
3. Structural Similarity Index (SSIM) - simplified version without using external libraries
4. Normalized Pearson Correlation Coefficient (NPCC)

You must implement these functions yourself using only NumPy (no OpenCV, skimage, etc).

Each function should be implemented as a helper function and called inside `compare_images(i1, i2)`.

Function signature:
    def compare_images(i1: np.ndarray, i2: np.ndarray) -> dict:

The return value should be like:
{
    "mse": float,
    "psnr": float,
    "ssim": float,
    "npcc": float
}

Assume that i1 and i2 are normalized grayscale images (values between 0 and 1).
"""

import numpy as np

def mse(i1: np.ndarray, i2: np.ndarray) -> float:
    """Mean Squared Error (MSE) - Erro Quadrático Médio (MSE) entre duas imagens"""
    return np.mean((i1 - i2) ** 2)

def psnr(i1: np.ndarray, i2: np.ndarray) -> float:
    """Peak Signal-to-Noise Ratio (PSNR) - Pico da Razão Sinal-Ruído (PSNR) entre duas imagens"""
    mse_value = mse(i1, i2)
    if mse_value == 0:
        return float('inf')
    return 10 * np.log10(1.0 / mse_value)

def ssim(i1: np.ndarray, i2: np.ndarray) -> float:
    """Structural Similarity Index (SSIM) - Índice de Similaridade Estrutural (SSIM) simplificado"""
    mean_i1, mean_i2 = np.mean(i1), np.mean(i2)
    var_i1, var_i2 = np.var(i1), np.var(i2)
    cov_i1_i2 = np.mean((i1 - mean_i1) * (i2 - mean_i2))
    
    c1, c2 = 1e-4, 1e-4  # Pequenos valores para evitar divisão por zero
    
    numerator = (2 * mean_i1 * mean_i2 + c1) * (2 * cov_i1_i2 + c2)
    denominator = (mean_i1**2 + mean_i2**2 + c1) * (var_i1 + var_i2 + c2)
    
    return numerator / denominator

def npcc(i1: np.ndarray, i2: np.ndarray) -> float:
    """Normalized Pearson Correlation Coefficient (NPCC) - Coeficiente de Correlação de Pearson Normalizado (NPCC)."""
    i1_mean, i2_mean = np.mean(i1), np.mean(i2)
    
    numerator = np.sum((i1 - i1_mean) * (i2 - i2_mean))
    denominator = np.sqrt(np.sum((i1 - i1_mean) ** 2) * np.sum((i2 - i2_mean) ** 2))
    
    if denominator != 0:
        return numerator / denominator
    else:
        return 0.0

def compare_images(i1: np.ndarray, i2: np.ndarray) -> dict:
    # Your implementation here
    return {
        "mse": mse(i1, i2),
        "psnr": psnr(i1, i2),
        "ssim": ssim(i1, i2),
        "npcc": npcc(i1, i2)
    }

if __name__ == "__main__":
    # Criando duas imagens de exemplo (100x100 pixels) com valores aleatórios
    img1 = np.random.rand(100, 100)
    img2 = np.random.rand(100, 100)

    results = compare_images(img1, img2)

    print("Resultados:")
    for metric, value in results.items():
        print(f"{metric}: {value:.4f}")
