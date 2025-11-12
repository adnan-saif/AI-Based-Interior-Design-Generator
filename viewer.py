import streamlit as st
import io
import time
import torch

def display_home_tab():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="main-header">AI Interior Design Studio</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style='font-size: 1.4rem; color: #5d6d7e; text-align: center; margin-bottom: 3rem; line-height: 1.6;'>
        Transform your space with the power of Artificial Intelligence. Upload your room photo and watch as AI redesigns it in your preferred style.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("https://cdn.pixabay.com/photo/2017/08/27/10/16/interior-2685521_1280.jpg", 
                use_container_width=True)
    

    st.markdown("---")
    st.markdown('<div class="sub-header">Design Statistics</div>', unsafe_allow_html=True)
    
    stats_cols = st.columns(3)
    with stats_cols[0]:
        st.markdown("""
        <div class="stat-card floating">
            <h3 style="font-size: 2.5rem; margin: 0;">25+</h3>
            <p style="font-size: 1.2rem;">Design Styles</p>
        </div>
        """, unsafe_allow_html=True)

    with stats_cols[1]:
        st.markdown("""
        <div class="stat-card floating" style="animation-delay: 0.5s;">
            <h3 style="font-size: 2.5rem; margin: 0;">100+</h3>
            <p style="font-size: 1.2rem;">Rooms Transformed</p>
        </div>
        """, unsafe_allow_html=True)
    
    with stats_cols[2]:
        st.markdown("""
        <div class="stat-card floating" style="animation-delay: 1s;">
            <h3 style="font-size: 2.5rem; margin: 0;">4K</h3>
            <p style="font-size: 1.2rem;">Output Quality</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Features Grid
    st.markdown("---")
    st.markdown('<div class="sub-header">Why Choose Our AI Designer</div>', unsafe_allow_html=True)
    
    features = [
        {"title": "🚀 Instant Transformation", "desc": "See your room redesigned in seconds with advanced AI algorithms"},
        {"title": "🎭 Multiple Styles", "desc": "Choose from 15+ interior design styles and customize to your preference"},
        {"title": "🏗️ Structure Aware", "desc": "AI preserves your room's architecture while transforming the interior"},
        {"title": "👨‍💻 Easy to Use", "desc": "No design experience required - simple three-step process"},
        {"title": "📸 High Quality", "desc": "4K resolution photorealistic renders that look like professional"},
        {"title": "🔄 Multiple Variations", "desc": "Generate different design options and choose your favorite"}
    ]
    
    cols = st.columns(3)
    for idx, feature in enumerate(features):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="feature-card">
                <h3 style="color: #2c3e50; margin-bottom: 1rem; font-size: 1.3rem;">{feature['title']}</h3>
                <p style="color: #5d6d7e; line-height: 1.6;">{feature['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<div class="sub-header">How It Works</div>', unsafe_allow_html=True)
    
    steps = [
        {"step": "📸", "title": "Upload Your Room", "desc": "Take a clear photo of your current space from a corner angle"},
        {"step": "🤖", "title": "AI Analysis", "desc": "Our AI analyzes room structure, depth, and architectural elements"},
        {"step": "🎨", "title": "Choose Style", "desc": "Select from various design preferences and customization options"},
        {"step": "✨", "title": "Generate Magic", "desc": "Watch as AI transforms your room with photorealistic results"}
    ]
    
    step_cols = st.columns(4)
    for idx, step in enumerate(steps):
        with step_cols[idx]:
            st.markdown(f"""
            <div class="design-card" style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 1rem; color: #3498db;">{step['step']}</div>
                <h4 style="color: #2c3e50; margin-bottom: 1rem; font-weight: 600;">{step['title']}</h4>
                <p style="color: #5d6d7e; line-height: 1.5;">{step['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    <div class="visual-section">
        <div style="text-align: center;">
            <h2 style="color: #2c3e50; margin-bottom: 1.5rem;">Ready to Transform Your Space?</h2>
            <p style="font-size: 1.3rem; color: #5d6d7e; margin-bottom: 2rem;">
            Join thousands of satisfied users who have redesigned their spaces with AI technology
            </p>
            <div class="stButton">
                <button style="font-size: 1.2rem; padding: 15px 40px;">Get Started Now</button>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def display_upload_tab(preprocessor):
    st.markdown('<div class="sub-header">Upload Your Room</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="upload-box">
        <h2 style="color: #2c3e50; margin-bottom: 1.5rem;">📤 Upload Your Room Photo</h2>
        <p style="color: #5d6d7e; font-size: 1.2rem; line-height: 1.6;">
        For optimal results, use a well-lit photo taken from room corner showing walls, floor, and main area. 
        Avoid blurry images and ensure good lighting conditions.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Drag and drop your room image here or click to browse", 
        type=['jpg', 'jpeg', 'png'], 
        label_visibility="collapsed"
    )
    
    if uploaded_file is not None:
        if (st.session_state.uploaded_image is None or 
            hasattr(uploaded_file, 'name') and (not hasattr(st.session_state, 'last_uploaded_name') or 
            st.session_state.last_uploaded_name != uploaded_file.name)):
            
            with st.spinner("🔄 Loading and processing your image..."):
                input_image = preprocessor.load_input(uploaded_file)
                st.session_state.processed_image = preprocessor.preprocess_image(input_image)
                st.session_state.uploaded_image = input_image
                st.session_state.last_uploaded_name = uploaded_file.name
            
            st.markdown("### Your Uploaded Room")
            st.image(input_image, width=950, caption="Original Room Image")
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i in range(100):
                progress_bar.progress(i + 1)
                status_text.text(f"Reading room structure... {i+1}%")
                time.sleep(0.02)
            
            with st.spinner("Creating depth map and analyzing room elements..."):
                st.session_state.depth_map = preprocessor.create_depth_map(st.session_state.processed_image)
                seg_map = preprocessor.run_segmentation_detection(st.session_state.processed_image)
                st.session_state.seg_visualization = preprocessor.visualize_segmentation_results(st.session_state.processed_image, seg_map)
                st.session_state.segmentation_done = True
            
        else:
            st.image(st.session_state.uploaded_image, width=950, caption="Your Uploaded Room")
        
        if st.session_state.segmentation_done:
            st.markdown("""
            <div class="visual-section">
                <div style="text-align: center;">
                    <h2 style="color: #2c3e50; margin-bottom: 1.5rem;">🎯 Room Analysis Results</h2>
                    <p style="font-size: 1.3rem; color: #5d6d7e; margin-bottom: 2rem;">
                    The AI has identified all key architectural elements and is ready for redesign.
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(" ")
            col1, col2 = st.columns([1, 1])

            with col1:
                st.image(st.session_state.seg_visualization, use_container_width=True, caption="🎨 Room Element Detection")
                st.markdown("""
                <div class="info-box">
                    <h4 style="color: #2c3e50; margin-bottom: 1rem;">🔍 Detected Elements</h4>
                    <p style="color: #5d6d7e; line-height: 1.6;">
                    The system analyzed your image and detected key room structures 
                    <span style="color: #e74c3c; font-weight: bold;">Walls</span>, 
                    <span style="color: #27ae60; font-weight: bold;">Floor</span>, 
                    <span style="color: #3498db; font-weight: bold;">Ceiling</span>, 
                    <span style="color: #9b59b6; font-weight: bold;">Doors</span>, 
                    and <span style="color: #f39c12; font-weight: bold;">Windows</span>. This ensures that the design transformation remains
                    realistic with original layout.
                    </p>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.image(st.session_state.depth_map, use_container_width=True, caption="📐 3D Depth Analysis")
                st.markdown("""
                <div class="info-box">
                    <h4 style="color: #2c3e50; margin-bottom: 1rem;">🌐 Spatial Mapping</h4>
                    <p style="color: #5d6d7e; line-height: 1.6;">Depth analysis ensures perfect preservation of room proportions and spatial relationships during redesign. The AI understands the 3D structure of your space.</p>
                </div>
                """, unsafe_allow_html=True)

def display_design_tab():
    st.markdown('<div class="sub-header">Design Configuration</div>', unsafe_allow_html=True)
    
    if not st.session_state.segmentation_done:
        st.markdown("""
        <div class="info-box">
            <h3 style="color: #2c3e50; margin-bottom: 1rem;">⚙️ Setup Required</h3>
            <p style="color: #5d6d7e; line-height: 1.6;">Please upload a room image in the Upload tab to begin designing your dream space. The AI needs to analyze your room structure first.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("#### Choose Your Design Style:")
        
        prompt_method = st.radio(
            "Prompt Configuration:",
            ["Use Predefined Options", "Custom Prompt"],
            horizontal=True,
            label_visibility="collapsed"
        )

        st.markdown(" ")

        if prompt_method == "Use Predefined Options":
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### Interior Design Style")
                style = st.selectbox("Select a design aesthetic:", 
                                   ["Minimalist", "Modern", "Bohemian", "Industrial", "Scandinavian", 
                                    "Rustic", "Futuristic", "Art Deco", "Vintage", "Japanese Zen"])
                
                st.markdown("#### Color Palette")
                color_scheme = st.selectbox("Choose a color scheme:", 
                                          ["Neutral", "Pastel", "Vibrant", "Monochrome", "Warm", 
                                           "Cool", "Earth Tones", "Jewel Tones"])
            
            with col2:
                st.markdown("#### Room Type")
                room_type = st.selectbox("Which room are you designing?", 
                                       ["Bedroom", "Living Room", "Bathroom", "Kitchen", "Office", 
                                        "Dining Room", "Studio"])
                
                st.markdown("#### Lighting Style")
                lighting = st.selectbox("Choose lighting ambience:", 
                                      ["Natural Light", "Warm Ambient", "Bright Overhead", 
                                       "Mood Lighting", "Studio Lighting"])
            

            prompt_parts = [
                f"Professional interior design of a {room_type} in {style} style",
                f"{color_scheme} color scheme",
                f"{lighting} lighting",
                "high quality, detailed, photorealistic, 4K resolution",
                "professional photography, architectural digest"
            ]
            prompt = ". ".join(prompt_parts)
            
        else:
            st.markdown("#### Describe Your Vision")
            custom_prompt = st.text_area("Custom Design Instruction:", 
                                       placeholder="Describe your desired interior design...",
                                       height=150)
            prompt = f"{custom_prompt}. photorealistic, high resolution, professional interior rendering." if custom_prompt else ""
        
        st.markdown(" ")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Design Scope")
            design_type = st.selectbox("Redesign Type:", 
                                     ["Interior Design only", "Full Architecture Change"])
            
            if design_type == "Interior Design only":
                prompt += ". Preserve room structure, walls, windows, and architectural elements. Change only furniture, decor, colors, and textures."
            else:
                prompt += ". Complete architectural redesign with new layout and structure."
        
        with col2:
            st.markdown("#### Output Options")
            num_images = st.selectbox("Number of Images to Generate:", 
                                      [1,2,3,4,5],
                                      index=2)
        
        st.session_state.prompt = prompt
        st.session_state.num_images = num_images
        st.session_state.design_type = design_type
        
        st.markdown("---")
        
        if st.button(
            "🚀 GENERATE DESIGNS", 
            type="primary", 
            use_container_width=True,
            key="generate_main"
        ):
            st.session_state.generate_designs = True
            st.rerun()

def display_results_tab(generator, postprocessor, llm_agent):
    st.markdown('<div class="sub-header">Your Generated Designs</div>', unsafe_allow_html=True)
    
    if st.session_state.get('generate_designs', False):
        st.session_state.generate_designs = False
        st.session_state.generated_images = []
        
        if not st.session_state.segmentation_done:
            st.warning("Please upload and process an image in the Upload tab first.")
        elif not st.session_state.get('prompt'):
            st.warning("Please configure settings in the Design tab first.")
        else:
            if st.session_state.design_type == "Interior Design only":
                controlnet_strength = 0.9
                generation_strength = 0.6
            else:
                controlnet_strength = 0.5
                generation_strength = 0.8
            
            negative_prompt = "low quality, blurry, distorted, bad anatomy, empty room, no furniture, poorly drawn, ugly, duplicate, morbid, mutilated, extra limbs, missing limbs, disfigured, deformed, body out of frame, bad hands, text, error, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, bad proportions, cloned face, disfigured, out of frame, ugly, extra limbs, bad anatomy, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, mutated hands, fused fingers, too many fingers"
            
            for i in range(1, st.session_state.num_images + 1):
                st.markdown(f"### Design {i}/{st.session_state.num_images}")
                
                with st.spinner(f"Generating design {i}... This may take a moment."):
                    seed = torch.randint(0, 100000, (1,)).item()
                    result_image = generator.generate_design_with_controlnet(
                        prompt=st.session_state.prompt,
                        input_image=st.session_state.processed_image,
                        depth_image=st.session_state.depth_map,
                        negative_prompt=negative_prompt,
                        strength=generation_strength,
                        controlnet_conditioning_scale=controlnet_strength,
                        guidance_scale=7.5,
                        seed=seed
                    )
                    
                    enhanced_image = postprocessor.enhance_image(result_image)
                    
                    st.session_state.generated_images.append(enhanced_image)
                    
                    st.image(enhanced_image, caption=f"Generated Design {i}", width=600)

                    with st.spinner("Generating description..."):
                        description = llm_agent.describe_image_with_gemini(enhanced_image)
                    
                    st.markdown("#### Description:")
                    st.markdown(f'<div class="ai-description">{description}</div>', unsafe_allow_html=True)
                
                    buf = io.BytesIO()
                    enhanced_image.save(buf, format="PNG")
                    st.download_button(
                        label=f"📥 Download Design {i}",
                        data=buf.getvalue(),
                        file_name=f"interior_design_{i}.png",
                        mime="image/png",
                        key=f"download_{i}",
                        use_container_width=True
                    )
                    
                    st.markdown("---")
            
            st.success(f"All {st.session_state.num_images} designs generated successfully!")
    
    elif st.session_state.generated_images:
        st.info("Previously generated designs:")
        for i, img in enumerate(st.session_state.generated_images, 1):
            st.subheader(f"Design {i}/{len(st.session_state.generated_images)}")
            st.image(img, caption=f"Generated Design {i}", width=600)
            
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            st.download_button(
                label=f"📥 Download Design {i}",
                data=buf.getvalue(),
                file_name=f"interior_design_{i}.png",
                mime="image/png",
                key=f"download_prev_{i}",
                use_container_width=True
            )
            
            st.markdown("---")
    
    elif not st.session_state.segmentation_done:
        st.markdown("""
        <div class="info-box">
            <h3 style="color: #2c3e50; margin-bottom: 1rem;">⚙️ Setup Required</h3>
            <p style="color: #5d6d7e; line-height: 1.6;">Please upload a room image in the Upload tab and configure your design preferences in the Design tab to generate amazing transformations of your space.</p>
        </div>
        """, unsafe_allow_html=True)
    elif not st.session_state.get('prompt'):
        st.markdown("""
        <div class="info-box">
            <h3 style="color: #2c3e50; margin-bottom: 1rem;">🎨 Design Configuration Needed</h3>
            <p style="color: #5d6d7e; line-height: 1.6;">Please configure your design settings in the Design tab first. Choose your preferred style, colors, and other preferences to create your perfect space.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="success-box">
            <h3 style="color: #2c3e50; margin-bottom: 1rem;">✅ Ready to Generate</h3>
            <p style="color: #5d6d7e; line-height: 1.6;">Your room has been analyzed and design preferences are set. Go to the Design tab and click the 'Generate Designs' button to create your transformed space.</p>
        </div>
        """, unsafe_allow_html=True)

def display_about_tab():
    st.markdown('<div class="sub-header">About AI Interior Design Studio</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box floating" style="animation-duration: 4s;">
        <h2 style="color: #2c3e50; margin-bottom: 1.5rem; background: linear-gradient(45deg, #3498db, #9b59b6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">🎨 Revolutionizing Interior Design with AI</h2>
        <p style="color: #5d6d7e; font-size: 1.1rem; line-height: 1.7;">
        Our AI Interior Design Studio leverages cutting-edge artificial intelligence to transform 
        your living spaces. Using advanced computer vision and generative AI models, we analyze 
        your room's architecture and create stunning, personalized design concepts in seconds.
        </p>
        <div style="background: linear-gradient(135deg, #3498db, #9b59b6); padding: 2px; border-radius: 10px; margin-top: 1.5rem;">
            <div style="background: white; padding: 1.5rem; border-radius: 8px;">
                <h4 style="color: #2c3e50; margin-bottom: 0.5rem;">✨ Why Choose Us?</h4>
                <p style="color: #5d6d7e; margin: 0;">Instant transformations • Professional quality • Unlimited creativity</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Technology Stack with Colorful Icons
    st.markdown('<div class="sub-header">Technology Stack</div>', unsafe_allow_html=True)
    
    tech_cols = st.columns(3)
    
    with tech_cols[0]:
        st.markdown("""
        <div class="feature-card floating" style="animation-duration: 3s; border-left: 5px solid #3498db;">
            <div style="background: linear-gradient(135deg, #3498db, #2980b9); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <span style="font-size: 2rem;">🤖</span>
            </div>
            <h3 style="color: #2c3e50; margin-bottom: 1rem;">Computer Vision</h3>
            <p style="color: #5d6d7e; line-height: 1.6;">
            • Room structure analysis<br>
            • Depth mapping<br>
            • Object detection<br>
            • Spatial understanding
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_cols[1]:
        st.markdown("""
        <div class="feature-card floating" style="animation-duration: 3s; animation-delay: 0.2s; border-left: 5px solid #9b59b6;">
            <div style="background: linear-gradient(135deg, #9b59b6, #8e44ad); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <span style="font-size: 2rem;">🎨</span>
            </div>
            <h3 style="color: #2c3e50; margin-bottom: 1rem;">Generative AI</h3>
            <p style="color: #5d6d7e; line-height: 1.6;">
            • Stable Diffusion<br>
            • ControlNet<br>
            • Style transfer<br>
            • Photorealistic rendering
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_cols[2]:
        st.markdown("""
        <div class="feature-card floating" style="animation-duration: 3s; animation-delay: 0.4s; border-left: 5px solid #e74c3c;">
            <div style="background: linear-gradient(135deg, #e74c3c, #c0392b); width: 60px; height: 60px; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <span style="font-size: 2rem;">⚡</span>
            </div>
            <h3 style="color: #2c3e50; margin-bottom: 1rem;">Real-time Processing</h3>
            <p style="color: #5d6d7e; line-height: 1.6;">
            • Instant previews<br>
            • Multiple variations<br>
            • High-resolution output<br>
            • Cloud optimization
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Mission & Vision with Gradient Backgrounds
    st.markdown('<div class="sub-header">Our Mission & Vision</div>', unsafe_allow_html=True)
    
    mission_cols = st.columns(2)
    
    with mission_cols[0]:
        st.markdown("""
        <div class="design-card floating" style="animation-duration: 3s; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 2.5rem;">
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h3 style="color: white; margin-bottom: 1.5rem; font-size: 1.8rem;">💡 Our Vision</h3>
                <p style="color: white; line-height: 1.7; font-size: 1.1rem;">
                To democratize interior design by making professional-grade design tools accessible to everyone. 
                We believe that everyone deserves to live in beautiful, well-designed spaces, regardless of 
                their budget or design experience.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with mission_cols[1]:
        st.markdown("""
        <div class="design-card floating" style="animation-duration: 3s; animation-delay: 0.3s; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 2.5rem;">
            <div style="background: rgba(255,255,255,0.1); padding: 1.5rem; border-radius: 15px; backdrop-filter: blur(10px);">
                <h3 style="color: white; margin-bottom: 1.5rem; font-size: 1.8rem;">🎯 Our Mission</h3>
                <p style="color: white; line-height: 1.7; font-size: 1.1rem;">
                To create the most intuitive and powerful AI-driven interior design platform that 
                transforms how people envision, plan, and execute their home design projects with 
                confidence and creativity.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Animated Features Grid
    st.markdown('<div class="sub-header">What Makes Us Unique</div>', unsafe_allow_html=True)
    
    features = [
        {
            "icon": "📸",
            "title": "Smart Room Analysis",
            "description": "Advanced AI analyzes your room's dimensions, lighting, and architectural features",
            "color": "#3498db"
        },
        {
            "icon": "🎭",
            "title": "15+ Design Styles",
            "description": "Choose from Minimalist, Modern, Bohemian, Industrial, Scandinavian and more",
            "color": "#9b59b6"
        },
        {
            "icon": "🏗️",
            "title": "Structure Preservation",
            "description": "Maintains room architecture while transforming interior elements",
            "color": "#e74c3c"
        },
        {
            "icon": "📐",
            "title": "3D Spatial Awareness",
            "description": "Depth mapping ensures realistic proportions and spatial relationships",
            "color": "#2ecc71"
        },
        {
            "icon": "🖼️",
            "title": "4K Photorealistic Renders",
            "description": "High-resolution outputs that look like professional photography",
            "color": "#f39c12"
        },
        {
            "icon": "⚡",
            "title": "Instant Generation",
            "description": "Multiple design variations generated in seconds, not weeks",
            "color": "#1abc9c"
        }
    ]
    
    # Display features in 2 columns with staggered animations
    feature_cols = st.columns(2)
    for idx, feature in enumerate(features):
        with feature_cols[idx % 2]:
            delay = (idx * 0.2)
            st.markdown(f"""
            <div class="info-box floating" style="margin-bottom: 1.5rem; animation-duration: 3s; animation-delay: {delay}s; border-left: 4px solid {feature['color']};">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <div style="background: {feature['color']}; width: 50px; height: 50px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 1rem;">
                        <span style="font-size: 1.5rem; filter: brightness(0) invert(1);">{feature['icon']}</span>
                    </div>
                    <h4 style="color: #2c3e50; margin: 0;">{feature['title']}</h4>
                </div>
                <p style="color: #5d6d7e; line-height: 1.6; margin: 0;">{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    
    # Animated connector lines
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <div style="display: flex; justify-content: space-between; align-items: center; max-width: 800px; margin: 0 auto;">
            <div style="flex: 1; height: 3px; background: linear-gradient(90deg, #3498db, #9b59b6); margin: 0 10px;"></div>
            <div style="flex: 1; height: 3px; background: linear-gradient(90deg, #9b59b6, #e74c3c); margin: 0 10px;"></div>
            <div style="flex: 1; height: 3px; background: linear-gradient(90deg, #e74c3c, #2ecc71); margin: 0 10px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Animated Footer
    st.markdown("""
    <div class="floating" style="text-align: center; padding: 3rem; background: linear-gradient(135deg, #2c3e50, #34495e); color: white; border-radius: 20px; margin-top: 2rem;">
        <h3 style="color: white; margin-bottom: 1rem;">🚀 Ready to Transform Your Space?</h3>
        <p style="color: rgba(255,255,255,0.8); font-size: 1.1rem; margin-bottom: 2rem;">
        Join thousands of users who have rediscovered their spaces with AI magic
        </p>
        <div style="display: inline-block; background: linear-gradient(135deg, #3498db, #9b59b6); padding: 12px 30px; border-radius: 25px; color: white; font-weight: bold; font-size: 1.1rem;">
            Start Your Design Journey
        </div>
        <div style="margin-top: 2rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.2);">
            <p style="font-size: 1.1rem; margin: 0.5rem 0;">Made with using Streamlit, PyTorch, and Stable Diffusion</p>
        </div>
    </div>
    """, unsafe_allow_html=True)