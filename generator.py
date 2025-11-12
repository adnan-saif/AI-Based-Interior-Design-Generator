import torch
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
from config import CONTROLNET_MODEL, STABLE_DIFFUSION_MODEL, DEFAULT_NUM_INFERENCE_STEPS, DEFAULT_GUIDANCE_SCALE

def setup_pipeline():
    """Setup ControlNet pipeline with depth control"""
    controlnet = ControlNetModel.from_pretrained(
        CONTROLNET_MODEL,
        torch_dtype=torch.float32
    )

    pipe = StableDiffusionControlNetPipeline.from_pretrained(
        STABLE_DIFFUSION_MODEL, 
        controlnet=controlnet,
        torch_dtype=torch.float32,
        safety_checker=None
    ).to("cpu")
    
    pipe.enable_attention_slicing()
    return pipe

def generate_design_with_controlnet(prompt, input_image, depth_image, negative_prompt="", 
                                  strength=0.8, guidance_scale=DEFAULT_GUIDANCE_SCALE, 
                                  controlnet_conditioning_scale=0.8, seed=None):
    """Generate design using ControlNet for better structure preservation"""
    pipe = setup_pipeline()
    
    generator = torch.Generator(device="cpu")
    if seed is not None:
        generator.manual_seed(seed)
    
    result = pipe(
        prompt=prompt,
        image=depth_image,
        num_inference_steps=DEFAULT_NUM_INFERENCE_STEPS,
        guidance_scale=guidance_scale,
        generator=generator,
        negative_prompt=negative_prompt,
        controlnet_conditioning_scale=controlnet_conditioning_scale,
        strength=strength
    ).images[0]
    
    return result