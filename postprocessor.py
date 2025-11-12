import cv2
import numpy as np
from PIL import Image

def enhance_image(image):
    """Enhance the generated image"""
    img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    enhanced = cv2.detailEnhance(img_cv, sigma_s=10, sigma_r=0.15)
    return Image.fromarray(cv2.cvtColor(enhanced, cv2.COLOR_BGR2RGB))