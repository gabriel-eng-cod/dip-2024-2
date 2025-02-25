import numpy as np
import cv2 as cv

def get_image_info(image):
    """
    Extracts metadata and statistical information from an image.

    Parameters:
    - image (numpy.ndarray): Input image.

    Returns:
    - dict: Dictionary containing image metadata and statistics.
    """
    
    ### START CODE HERE ###
    height, width = image.shape[:2]
    dtype = image.dtype
    depth = image.itemsize * 8
    min_val = image.min()
    max_val = image.max()
    mean_val = image.mean()
    std_val = image.std()
    ### END CODE HERE ###

    return {
        "width": width,
        "height": height,
        "dtype": dtype,
        "depth": depth,
        "min_value": min_val,
        "max_value": max_val,
        "mean": mean_val,
        "std_dev": std_val
    }

# Example Usage:
sample_image = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
info = get_image_info(sample_image)

# Print results
for key, value in info.items():
    print(f"{key}: {value}")

cv.imshow("Image", sample_image)
cv.waitKey(0)
cv.destroyAllWindows()