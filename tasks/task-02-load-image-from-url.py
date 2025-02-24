import argparse
import numpy as np
import cv2 as cv
import requests

def load_image_from_url(url, **kwargs):
    """
    Loads an image from an Internet URL with optional arguments for OpenCV's cv.imdecode.
    
    Parameters:
    - url (str): URL of the image.
    - **kwargs: Additional keyword arguments for cv.imdecode (e.g., flags=cv.IMREAD_GRAYSCALE).
    
    Returns:
    - image: Loaded image as a NumPy array.
    """
    
    ### START CODE HERE ###
    response = requests.get(url, stream=True)
    response.raise_for_status()
    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    image = cv.imdecode(image_array, kwargs.get("flags", cv.IMREAD_COLOR))
    return image
    ### END CODE HERE ###


image = load_image_from_url('https://static.nationalgeographicbrasil.com/files/styles/image_3200/public/nationalgeographic_2788792_0.webp?w=1600&h=900')
cv.imshow("Image", image)
cv.waitKey(0)
cv.destroyAllWindows()
    