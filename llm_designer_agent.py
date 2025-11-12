import google.generativeai as genai

def describe_image_with_gemini(image):
    """Describe image using Gemini"""
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = """
    Describe this image in a detailed paragraph of 100 words. Mention:
    - Objects visible
    - Colors & textures  
    - Lighting & ambience
    - Interior style (if room)
    - Overall scene summary
    """
    response = model.generate_content([prompt, image])
    return response.text