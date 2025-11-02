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
st.set_page_config(page_title="TechSmashers", page_icon=":tada:", layout="wide")

# Custom CSS including updated right vertical navbar
st.markdown("""
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">

<style>
html {
    scroll-behavior: smooth;
}
body {
    background-color: #f8f9fa;
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
    flex-direction: row-reverse;  /* Change direction to reverse, so the label is placed on the left of the icon */
    align-items: center;  /* Align items horizontally */
    text-decoration: none;
    color: #333;
    font-size: 20px;
    position: relative;
    padding: 5px 0; /* Add padding to create space around the icon */
}
.vertical-nav a:hover {
    color: #d2691e;
    transform: scale(1.15);
}
.vertical-nav a span {
    font-size: 12px;
    margin-right: 8px;  /* Add right margin to space the label from the icon */
    opacity: 0;
    transform: translateX(-10px);
    transition: all 0.3s ease-in-out;
    background-color: #fff;
    padding: 4px 8px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.15);
    position: absolute;
    top: 50%;  /* Adjust this to control vertical position */
    left: 50%;  /* Center horizontally */
    transform: translateX(-50%) translateY(-50%);  /* Correctly center both horizontally and vertically */
    white-space: nowrap;
}
.vertical-nav a:hover span {
    opacity: 1;
    transform: translateX(-50%) translateY(-50%);  /* Ensure the label stays centered */
}
</style>

<div class="vertical-nav">
    <a href="#home"><i class="fas fa-house"></i><span>Home</span></a>
    <a href="#try"><i class="fas fa-play-circle"></i><span>Try</span></a>
    <a href="#demo"><i class="fas fa-cogs"></i><span>Demo</span></a> <!-- Demo section link -->
</div>
""", unsafe_allow_html=True)

# ============================ HOME SECTION ========================================
with st.container():
    #st.write("##")
    st.markdown('<div id="home"></div>', unsafe_allow_html=True)
    st.header("Welcome to 2D to 3D Assets Generator :wave:")
    st.title("Bring Your 2D Designs to Life in 3D!")
    st.write("Instantly transform 2D images into fully-realized 3D assets with our AI-powered generator. Whether you're a game developer, artist, or designer, bring your concepts to life with just a few clicks—no 3D modeling skills required.")

# ============================ FEATURES SECTION ========================================
with st.container():
    st.write("_______________________________________________")
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader(":thinking_face: What does the tool do?")
        st.markdown("""
        - 🧠 **Analyzes** 2D images (like concept sketches, sprites, or photos)  
        - 🧩 **Estimates** depth, shape, and structure using AI  
        - 🎨 **Generates** 3D meshes with textures, lighting, and details  
        - 🚀 **Outputs** assets ready for games, animation, AR/VR  
        """)

    with right_column:
        st_lottie(path1, height=300, width=600, key="coding1")

# ============================ WHO SECTION ========================================
with st.container():
    st.write("_______________________________________________")
    left_column, right_column = st.columns(2)

    with left_column:
        st_lottie(path2, height=300, width=600, key="coding2")

    with right_column:
        st.subheader(":thinking_face: Who uses the tool?")
        st.markdown("""
        - 🎮 **Game Developers** – Quickly prototype or generate game-ready assets  
        - 🧑‍🎨 **3D Artists** – Use as a starting point for detailed modeling  
        - ✏️ **Designers & Illustrators** – Visualize 2D work in 3D effortlessly  
        - 🌐 **AR/VR Creators** – Populate virtual worlds faster with ready assets  
        """)

# ============================ WHY SECTION ========================================
with st.container():
    st.write("_______________________________________________")
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader(":thinking_face: Why it's useful?")
        st.markdown("""
        - ⏱️ **Saves time and effort** compared to manually modeling from scratch  
        - 🌉 **Bridges the gap** between 2D art and 3D content creation  
        - 🙌 **Makes 3D accessible** to people without technical 3D modeling skills  
        """)

    with right_column:
        st_lottie(path3, height=300, width=600, key="coding3")

# ============================ DEMO SECTION ========================================
with st.container():
    st.write("##")
    st.markdown('<div id="demo"></div>', unsafe_allow_html=True)  # Anchor for Demo section
    st.markdown("""
        <div style="background-color: #fff7f0; padding: 60px 40px; border-radius: 15px; box-shadow: 0 6px 16px rgba(0,0,0,0.1);">
            <h2 style="text-align:center; color:#d2691e;">🎬 Demo: 2D to 3D Transformation</h2>
            <p style="text-align:center; font-size:18px; max-width: 800px; margin: 20px auto;">
                Watch how your 2D images transform into stunning 3D assets using our AI-powered generator! Check out the demo to get a feel of the tool’s capabilities.
            </p>
            <div style="text-align:center; width: 100%; height: auto; display: flex; justify-content: center;">
                <img src="https://i.imgur.com/vE28xUy.gif" alt="Demo of 2D to 3D transformation" style="width: 100%; max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);" />
            </div>
        </div>
    """, unsafe_allow_html=True)

# ============================ TRY SECTION ========================================
with st.container():
    st.write("##")
    st.markdown('<div id="try"></div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="background-color: #fff7f0; padding: 60px 40px; border-radius: 15px; box-shadow: 0 6px 16px rgba(0,0,0,0.1);">
            <h2 style="text-align:center; color:#d2691e;">🚀 Ready to Try the Tool?</h2>
            <p style="text-align:center; font-size:18px; max-width: 800px; margin: 20px auto;">
                Transform your 2D artwork into stunning 3D models in just a few clicks! Whether you're prototyping game assets, building a VR scene, or just exploring AI tools — our intuitive interface makes the process seamless.
            </p>
            <p style="text-align:center; font-size:16px; color: #444; max-width: 800px; margin: 10px auto;">
                Click the button below to access the tool. You’ll be able to upload your image, process it through our AI engine, and preview the 3D output live in your browser.
            </p>
            <div style="text-align:center; margin-top: 30px;">
                <a href="WebpgMain.html" target="_blank">
                    <button style="background-color:#d2691e; color:white; font-size:18px; padding:14px 28px; border:none; border-radius:10px; cursor:pointer; box-shadow: 0 4px 10px rgba(0,0,0,0.15); transition: 0.3s ease;">
                        Try the Tool ↗
                    </button>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ============================ FAQ BUTTON ==========================================
st.markdown("""
    <style>
        .faq-button {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #d2691e;
            color: white;
            font-size: 24px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            border: none;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease-in-out;
        }

        .faq-button:hover {
            transform: scale(1.2);
            background-color: #ff8c00;
        }

        .faq-button:active {
            transform: scale(1.1);
        }

        .faq-button i {
            font-size: 24px;
        }
    </style>
    <a href="#faq-section" class="faq-button">
        <i class="fas fa-question"></i>
    </a>
""", unsafe_allow_html=True)

# ============================ FAQ SECTION ========================================
with st.container():
    st.markdown('<div id="faq-section"></div>', unsafe_allow_html=True)  # Anchor for FAQ section
    st.markdown("<h2 style='text-align: center; color: #d2691e;'>📚 Frequently Asked Questions</h2>", unsafe_allow_html=True)

    st.markdown("""
        <style>
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

        <div class="faq-entry">
            <div class="faq-question">📁 What image formats are supported?</div>
            <div class="faq-answer">We support PNG, JPG, and BMP formats. For best results, use high-resolution images with clear outlines.</div>
        </div>

        <div class="faq-entry">
            <div class="faq-question">🎨 How detailed should my 2D image be?</div>
            <div class="faq-answer">While our AI works on all images, high-contrast, uncluttered images give the most accurate 3D reconstructions.</div>
        </div>

        <div class="faq-entry">
            <div class="faq-question">🔄 Can I export the 3D model to Blender or Unity?</div>
            <div class="faq-answer">Yes! You can download your 3D model in formats compatible with Blender, Unity, and other platforms.</div>
        </div>

        <div class="faq-entry">
            <div class="faq-question">⏱️ How long does the conversion take?</div>
            <div class="faq-answer">On average, it takes 5–15 seconds depending on image complexity and current load.</div>
        </div>

        <div class="faq-entry">
            <div class="faq-question">🔒 Is my image data stored or shared?</div>
            <div class="faq-answer">No, your images are processed securely and are not stored after processing. Your privacy is a priority.</div>
        </div>
    """, unsafe_allow_html=True)
