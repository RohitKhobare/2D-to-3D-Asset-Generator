import json
import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie

# Load Lottie animations
def load_lottie(path: str):
    with open(path, "r") as f:
        return json.load(f)

# Animations
path1 = load_lottie("./ani1.json")
path2 = load_lottie("./ani2.json")
path3 = load_lottie("./ani3.json")

# Page Config
st.set_page_config(page_title="PBL Project", page_icon=":tada:", layout="wide")

# Custom CSS for style
st.markdown("""
    <style>
    html {
        scroll-behavior: smooth;
    }
    .vertical-nav {
        position: fixed;
        top: 50%;
        right: 10px;
        transform: translateY(-50%);
        display: flex;
        flex-direction: column;
        gap: 25px;
        z-index: 999;
    }
    .vertical-nav a {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        text-decoration: none;
        color: #333;
        font-size: 20px;
        position: relative;
        transition: transform 0.3s, color 0.3s;
    }
    .vertical-nav a:hover {
        color: #d2691e;
        transform: scale(1.15);
    }
    .vertical-nav a span {
        font-size: 12px;
        position: absolute;
        top: 50%;
        right: 100%;
        transform: translateY(-50%) translateX(10px);
        background-color: #fff;
        color: #333;
        padding: 4px 8px;
        border-radius: 8px;
        white-space: nowrap;
        box-shadow: 0 2px 5px rgba(0,0,0,0.15);
        opacity: 0;
        transition: all 0.3s ease-in-out;
    }
    .vertical-nav a:hover span {
        opacity: 1;
        transform: translateY(-50%) translateX(0);
    }

    .faq-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #d2691e;
        color: white;
        border: none;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        font-size: 24px;
        cursor: pointer;
        z-index: 1000;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease;
    }

    /* Hover effect */
    .faq-button:hover {
        background-color: #a45110;
    }

    /* Active effect on click */
    .faq-button:active {
        transform: scale(0.95);
    }

    .image-row {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin-top: 30px;
        flex-wrap: wrap;
    }

    .image-row img {
        max-width: 100%;
        height: auto;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    .caption {
        text-align: center;
        margin-top: 10px;
        font-weight: 500;
        font-size: 16px;
    }

    .faq-entry {
        background-color: #fff7f0;
        border-left: 5px solid #d2691e;
        padding: 20px;
        margin: 20px 0;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }

    .faq-entry:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.1);
    }

    .faq-question {
        font-size: 18px;
        font-weight: 600;
        color: #333;
        margin-bottom: 8px;
    }

    .faq-answer {
        font-size: 15px;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)

# HOME SECTION
with st.container():
    st.markdown('<div id="home"></div>', unsafe_allow_html=True)
    st.markdown("##")
    st.header("Welcome to 2D to 3D Assets Generator :wave:")
    st.title("Bring Your 2D Designs to Life in 3D!")
    st.write("Instantly transform 2D images into fully-realized 3D assets with our AI-powered generator.")
    st.markdown("---")

# TECHSMASHERS HIGHLIGHT
with st.container():
    st.markdown("<h3 style='text-align: center; color: #d2691e;'>Powered by Team <strong>TechSmashers</strong></h3>", unsafe_allow_html=True)
    st.markdown("---")

# FEATURES SECTION
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader(":thinking_face: What does the tool do?")
        st.markdown("""- 🧠 **Analyzes** 2D images
                      - 🧩 **Estimates** depth and structure
                      - 🎨 **Generates** 3D meshes
                      - 🚀 **Outputs** assets for games, AR/VR""")
    with right_column:
        st_lottie(path1, height=300, key="ani1")
    st.markdown("---")

# WHO SECTION
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(path2, height=300, key="ani2")
    with right_column:
        st.subheader(":thinking_face: Who uses the tool?")
        st.markdown("""- 🎮 **Game Developers**
                      - 🧑‍🎨 **3D Artists**
                      - ✏️ **Designers & Illustrators**
                      - 🌐 **AR/VR Creators""")
    st.markdown("---")

# FAQ SECTION
with st.container():
    st.markdown('<div id="faq-section"></div>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #d2691e;'>📚 Frequently Asked Questions</h2>", unsafe_allow_html=True)

    st.markdown("""
        <div class="faq-entry">
            <div class="faq-question">📁 What image formats are supported?</div>
            <div class="faq-answer">We support PNG, JPG, and BMP formats. For best results, use high-resolution images with clear outlines.</div>
        </div>

        <div class="faq-entry">
            <div class="faq-question">🎨 How detailed should my 2D image be?</div>
            <div class="faq-answer">While our AI works on all images, high-contrast, uncluttered images give the most accurate 3D reconstructions.</div>
        </div>
    """, unsafe_allow_html=True)

# FAQ Button Scroll
st.markdown("""
    <button class="faq-button" onclick="document.getElementById('faq-section').scrollIntoView({ behavior: 'smooth' });">?</button>
""", unsafe_allow_html=True)
