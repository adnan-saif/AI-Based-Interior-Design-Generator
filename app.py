import streamlit as st
from theme_config_css import CSS_STYLES
from viewer import display_home_tab, display_upload_tab, display_design_tab, display_results_tab, display_about_tab
import preprocessor
import generator
import postprocessor
import llm_designer_agent

# Apply CSS styles
st.markdown(CSS_STYLES, unsafe_allow_html=True)

# ----------------- Streamlit UI ----------------- #
st.set_page_config(
    page_title="AI Interior Design Generator", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None
if 'segmentation_done' not in st.session_state:
    st.session_state.segmentation_done = False
if 'depth_map' not in st.session_state:
    st.session_state.depth_map = None
if 'processed_image' not in st.session_state:
    st.session_state.processed_image = None
if 'seg_visualization' not in st.session_state:
    st.session_state.seg_visualization = None
if 'generated_images' not in st.session_state:
    st.session_state.generated_images = []

# Tab structure
tab_home, tab1, tab2, tab3, tab_about = st.tabs(["Home", "Upload", "Design", "Results", "About"])

with tab_home:
    display_home_tab()

with tab1:
    display_upload_tab(preprocessor)

with tab2:
    display_design_tab()

with tab3:
    display_results_tab(generator, postprocessor, llm_designer_agent)

with tab_about:
    display_about_tab()

