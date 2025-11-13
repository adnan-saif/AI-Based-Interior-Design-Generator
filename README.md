# 🏡 AI-Based Interior Design Generator with ControlNet

## 📘 Introduction

The **AI-Based Interior Design Generator** is an advanced generative AI system that transforms normal room photos into high-quality, realistic, and stylistically enhanced interior designs.  
It utilizes **Stable Diffusion with ControlNet** for structure-preserving image generation, **semantic segmentation** for room element detection, and **depth estimation** for spatial accuracy.  
Additionally, the project integrates **Google’s Gemini 2.0 Flash** model to describe the generated designs with natural language insights.

---

## 🎯 Objectives

- Generate realistic and customized **interior designs** using AI-driven image generation.  
- Utilize **ControlNet** and **depth estimation** to maintain architectural structure.  
- Apply **semantic segmentation** to detect room elements like walls, floors, and windows.  
- Offer multiple **style**, **color scheme**, and **lighting** configurations.  
- Automatically generate **AI-based image descriptions** using Google Gemini.  

---

## 🧰 Technologies Used

- **Programming Language**: Python  
- **Generative Models**:
  - Stable Diffusion v1.5  
  - ControlNet (Depth-based Conditioning)  
- **AI Models**:
  - MiDaS (Depth Estimation)  
  - Mask2Former (Semantic Segmentation)  
  - Google Gemini 2.0 Flash (Image Description)  
- **Libraries/Frameworks**:
  - diffusers  
  - transformers  
  - torch  
  - OpenCV  
  - numpy, matplotlib, Pillow (Image Processing)  
- **IDE/Tools**: VS Code, Jupyter Notebook  

---

## 🧠 Workflow Overview

| Step | Module | Description |
|------|---------|-------------|
| 1️⃣ | **Preprocessing** | Resize and normalize input room image |
| 2️⃣ | **Segmentation** | Detect structural elements (walls, floor, ceiling, windows, doors) using Mask2Former |
| 3️⃣ | **Depth Map Creation** | Generate depth map with MiDaS for spatial consistency |
| 4️⃣ | **Design Generation** | Generate interior design using Stable Diffusion + ControlNet |
| 5️⃣ | **Enhancement** | Apply OpenCV filters for detail enhancement |
| 6️⃣ | **AI Description** | Generate descriptive text using Google Gemini |

---

## 💻 Application Features

### 🖼️ Intelligent Image Transformation
- Converts a plain room image into a **stylized and photorealistic design**.  
- Supports **two generation types**:
  - *Interior Redesign (Preserve Structure)*  
  - *Full Architecture Change*  

### 🎨 Customization Options
- Choose from:
  - **10 Interior Styles** (Minimalist, Modern, Bohemian, etc.)  
  - **7 Room Types** (Bedroom, Kitchen, Office, etc.)  
  - **8 Color Schemes** (Neutral, Pastel, Vibrant, etc.)  
  - **5 Lighting Styles** (Natural, Ambient, Studio, etc.)  

### 🧩 AI Segmentation
- Detects and visualizes structural components using **semantic segmentation** with color overlays.  

### 🌈 Depth-Guided Generation
- Uses **ControlNet (Depth)** to maintain layout and geometry of the original room while enhancing the design.  

### 🪄 Automated Description
- Each generated design is described automatically by **Gemini 2.0 Flash**, providing:
  - Objects present  
  - Colors and textures  
  - Lighting and ambience  
  - Interior style summary  

---

## 🧭 How to Use

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/AI-Interior-Design-Generator.git
    cd AI-Interior-Design-Generator
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Add Your Google API Key**

    - Open the script and replace:
      ```python
      genai.configure(api_key="Paste_Your_API_Key_Here")
      ```
      with your actual Google Gemini API key.

4. **Run the Application**

    ```bash
    python app.py
    ```

5. **Follow On-Screen Prompts**
    - Enter your input image path.  
    - Choose between **custom instructions** or **predefined style options**.  
    - View and save generated designs with detailed AI-based descriptions.  

---

## ✅ Results

- **Photorealistic AI interior designs** generated from real room photos.  
- **Structure-preserving transformations** using ControlNet depth guidance.  
- **Automatic segmentation visualization** of room elements.  
- **Natural language design descriptions** powered by Gemini.  
- Multiple configurable options for user creativity and experimentation.  

---

## 🔮 Future Work

- Integration with **Streamlit Web Interface** for real-time design generation.  
- Addition of **furniture placement optimization** using scene understanding.  
- Support for **multi-view generation** and **3D layout exports**.  
- Integration with **text-to-3D or AR visualization tools**.  

---

## 📚 References

- [Stable Diffusion (Hugging Face)](https://huggingface.co/runwayml/stable-diffusion-v1-5)  
- [ControlNet Depth Model](https://huggingface.co/lllyasviel/sd-controlnet-depth)  
- [Mask2Former Segmentation Model](https://huggingface.co/facebook/mask2former-swin-large-ade-semantic)  
- [MiDaS Depth Estimation](https://huggingface.co/Intel/dpt-large)  
- [Google Gemini API](https://ai.google.dev/gemini-api/docs)  

---

## 📦 Clone Repository

```bash
git clone https://github.com/your-username/AI-Interior-Design-Generator.git
