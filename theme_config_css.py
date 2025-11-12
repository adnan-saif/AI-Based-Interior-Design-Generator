CSS_STYLES = """
<style>
    /* Main styling - Enhanced Clean White Theme */
    .main {
        background-color: #ffffff;
    }
    
    /* Animated Gradient Header */
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #2c3e50, #3498db, #9b59b6, #e74c3c);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 700;
        padding: 1rem;
        animation: gradientShift 8s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .sub-header {
        font-size: 2rem;
        color: #2c3e50;
        border-bottom: 3px solid #3498db;
        padding-bottom: 0.8rem;
        margin-bottom: 2rem;
        font-weight: 600;
        position: relative;
        overflow: hidden;
    }
    
    .sub-header::after {
        content: '';
        position: absolute;
        bottom: -3px;
        left: -100%;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, transparent, #e74c3c, transparent);
        animation: slideLine 3s ease-in-out infinite;
    }
    
    @keyframes slideLine {
        0% { left: -100%; }
        50% { left: 100%; }
        100% { left: 100%; }
    }
    
    /* Enhanced Cards with 3D Effects */
    .feature-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        color: #2c3e50;
        padding: 2.5rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 1px solid #e1e8ed;
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(52, 152, 219, 0.1), transparent);
        transition: left 0.5s ease;
    }
    
    .feature-card:hover::before {
        left: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
    }
    
    .info-box {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        color: #2c3e50;
        padding: 2.5rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
        border: 1px solid #e1e8ed;
        transition: all 0.3s ease;
    }
    
    .info-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.12);
    }
    
    .success-box {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        color: #2c3e50;
        padding: 2.5rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
        border: 1px solid #e1e8ed;
        animation: pulseGlow 2s ease-in-out infinite alternate;
    }
    
    @keyframes pulseGlow {
        from { box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08); }
        to { box-shadow: 0 8px 30px rgba(52, 152, 219, 0.2); }
    }
    
    .upload-box {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border: 3px dashed #3498db;
        border-radius: 25px;
        padding: 4rem;
        text-align: center;
        margin-bottom: 3rem;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.1);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        color: #2c3e50;
        position: relative;
        overflow: hidden;
    }
    
    .upload-box::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(transparent, rgba(52, 152, 219, 0.1), transparent 30%);
        animation: rotateBorder 4s linear infinite;
    }
    
    @keyframes rotateBorder {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .upload-box:hover {
        transform: scale(1.03) translateY(-5px);
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.15);
        border-color: #e74c3c;
    }
    
    /* Enhanced Tabs with Glass Morphism - Remove Extra Right Space */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
        width: fit-content !important;
        max-width: 100% !important;
        justify-content: flex-start !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 52px;
        white-space: nowrap;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 13px;
        padding: 12px 22px;
        color: #2c3e50;
        font-weight: 600;
        font-size: 2rem;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 1px solid rgba(255, 255, 255, 0.3);
        position: relative;
        overflow: hidden;
        flex-shrink: 0;
    }
    
    .stTabs [data-baseweb="tab"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
        transition: left 0.5s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover::before {
        left: 100%;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 10px 25px rgba(52, 152, 219, 0.3);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3498db, #2980b9);
        color: white;
        box-shadow: 0 8px 25px rgba(52, 152, 219, 0.4);
        transform: translateY(-2px);
    }
            
    /* Remove all possible bottom borders */
    .stTabs [data-baseweb="tab-border"] {
        display: none !important;
    }

    .stTabs [data-baseweb="tab-highlight"] {
        background-color: transparent;
        display: none !important;
    }
    
    /* Remove the empty space container after tabs */
    .stTabs [data-baseweb="tab-list"] > :last-child {
        display: none !important;
    }
    
    /* Enhanced Buttons with Ripple Effect */
    .stButton button {
        background: linear-gradient(135deg, #3498db, #2980b9);
        color: white;
        border: none;
        padding: 15px 35px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 30px;
        font-weight: 600;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 6px 20px rgba(52, 152, 219, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .stButton button::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        transform: translate(-50%, -50%);
        transition: width 0.6s ease, height 0.6s ease;
    }
    
    .stButton button:hover::after {
        width: 300px;
        height: 300px;
    }
    
    .stButton button:hover {
        transform: translateY(-5px) scale(1.05);
        box-shadow: 0 12px 30px rgba(52, 152, 219, 0.6);
        background: linear-gradient(135deg, #2980b9, #2573a7);
    }
    
    /* Progress bars with Animation */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #3498db 0%, #2980b9 50%, #9b59b6 100%);
        background-size: 200% 100%;
        animation: progressAnimation 2s ease-in-out infinite;
    }
    
    @keyframes progressAnimation {
        0% { background-position: 200% 0; }
        100% { background-position: -200% 0; }
    }
    
    /* Enhanced Image styling with Parallax Effect */
    .generated-image {
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        margin: 2rem 0;
        border: 3px solid #3498db;
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    
    .generated-image::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(52, 152, 219, 0.1), rgba(155, 89, 182, 0.1));
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .generated-image:hover::before {
        opacity: 1;
    }
    
    .generated-image:hover {
        transform: scale(1.05) rotate(1deg);
        box-shadow: 0 25px 50px rgba(0,0,0,0.3);
    }
    
    /* Enhanced Text areas and inputs */
    .stTextArea textarea, .stTextInput input {
        border-radius: 15px;
        border: 2px solid #e1e8ed;
        padding: 18px;
        font-size: 16px;
        transition: all 0.3s ease;
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(5px);
    }
    
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: #3498db;
        box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.2);
        transform: translateY(-2px);
    }
    
    /* File uploader with Enhanced Style */
    .stFileUploader {
        border: 3px dashed #3498db;
        border-radius: 20px;
        padding: 30px;
        background: rgba(52, 152, 219, 0.05);
        backdrop-filter: blur(5px);
        transition: all 0.3s ease;
    }
    
    .stFileUploader:hover {
        border-color: #e74c3c;
        background: rgba(231, 76, 60, 0.05);
    }
    
    /* Enhanced Metrics and stats */
    .stMetric {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        color: #2c3e50;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        border: 1px solid #e1e8ed;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .stMetric::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(52, 152, 219, 0.1), transparent);
        transform: rotate(45deg);
        transition: all 0.3s ease;
    }
    
    .stMetric:hover::before {
        transform: rotate(45deg) translate(50%, 50%);
    }
    
    .stMetric:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
    }
    
    /* Custom backgrounds for different sections */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        background-attachment: fixed;
    }
    
    /* Enhanced Radio buttons */
    .stRadio > div {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
    }
    
    /* Enhanced Select boxes */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(5px);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Enhanced Sliders */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #3498db, #9b59b6);
    }
    
    /* Enhanced Expander */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border: 1px solid #e1e8ed;
        border-radius: 15px;
        transition: all 0.3s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        transform: translateY(-2px);
    }
    
    /* Visual enhancements */
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin: 10px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.15);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: rgba(255, 255, 255, 0.1);
        transform: rotate(45deg);
        transition: all 0.3s ease;
    }
    
    .stat-card:hover::before {
        transform: rotate(45deg) translate(50%, 50%);
    }
    
    .stat-card:hover {
        transform: translateY(-10px) scale(1.05);
        box-shadow: 0 20px 40px rgba(0,0,0,0.25);
    }
    
    .visual-section {
        background: linear-gradient(135deg, rgba(245, 247, 250, 0.9) 0%, rgba(195, 207, 226, 0.9) 100%);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 25px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .visual-section:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
    }
    
    .design-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: 0 12px 30px rgba(0,0,0,0.1);
        border: 1px solid #e1e8ed;
        transition: all 0.3s ease;
    }
    
    .design-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 18px 40px rgba(0,0,0,0.15);
    }
    
    .ai-description {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-left: 5px solid #3498db;
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        font-style: italic;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        transition: all 0.3s ease;
    }
    
    .ai-description:hover {
        transform: translateX(5px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
    }
    
    /* Floating Animation */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    .floating {
        animation: float 3s ease-in-out infinite;
    }
    
    /* Typewriter Effect */
    .typewriter {
        overflow: hidden;
        border-right: 3px solid #3498db;
        white-space: nowrap;
        margin: 0 auto;
        animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;
    }
    
    @keyframes typing {
        from { width: 0 }
        to { width: 100% }
    }
    
    @keyframes blink-caret {
        from, to { border-color: transparent }
        50% { border-color: #3498db; }
    }
    
    /* Particle Background Effect */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    
    .particle {
        position: absolute;
        background: rgba(52, 152, 219, 0.1);
        border-radius: 50%;
        animation: floatParticle 20s infinite linear;
    }
    
    @keyframes floatParticle {
        0% { transform: translateY(100vh) translateX(0); }
        100% { transform: translateY(-100vh) translateX(100px); }
    }
</style>
"""