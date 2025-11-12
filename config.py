import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure with hardcoded API key
genai.configure(api_key = API_KEY)

# Model configurations
SEGMENTATION_MODEL_NAME = "facebook/mask2former-swin-large-ade-semantic"
CONTROLNET_MODEL = "lllyasviel/sd-controlnet-depth"
STABLE_DIFFUSION_MODEL = "runwayml/stable-diffusion-v1-5"
DEPTH_ESTIMATION_MODEL = "Intel/dpt-large"

# Segmentation labels and colors
LABELS = {
    "wall": 0,
    "floor": 3,
    "ceiling": 5,
    "window": 8,
    "door": 14,
}

COLORS = {
    "wall": (255, 0, 0),
    "floor": (0, 255, 0),
    "ceiling": (0, 0, 255),
    "window": (255, 255, 0),
    "door": (255, 0, 255),
}

# Generation parameters
ALPHA = 0.35
DEFAULT_IMAGE_SIZE = (512, 512)
DEFAULT_NUM_INFERENCE_STEPS = 30
DEFAULT_GUIDANCE_SCALE = 7.5