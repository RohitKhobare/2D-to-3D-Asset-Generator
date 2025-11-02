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

# Custom CSS
st.markdown("""
    <style>
    html {
        scroll-behavior: smooth;
    }

    body {
        background-color: #f8f9fa;
    }

    /* Semi-circular nav */
    .nav-container {
        position: fixed;
        top: 30px;
        right: 0;
        width: 100px;
        height: 250px;
        background: linear-gradient(135deg, #ffecd2, #fcb69f);
        border-top-left-radius: 125px;
        border-bottom-left-radius: 125px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        z-index: 1000;
        box-shadow: -4px 4px 10px rgba(0,0,0,0.2);
    }

    .nav-button {
        background: none;
        border: none;
        margin: 10px 0;
        font-size: 18px;
        cursor: pointer;
        color: #333;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    .nav-button:hover {
        transform: scale(1.1);
        color: #d2691e;
    }

    button:hover {
    background-color: cyan;
    transform: translateY(-2px);
    }

    </style>

    <div class="nav-container">
        <a href="#home"><button class="nav-button">Home</button></a>
        <a href="#try"><button class="nav-button">Try</button></a>
        <a href="#team"><button class="nav-button">Team</button></a>
    </div>
""", unsafe_allow_html=True)

# ============================ HOME SECTION ========================================
with st.container():
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

# ============================ TRY BUTTON SECTION ========================================
with st.container():
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

# ============================ TEAM SECTION ========================================
with st.container():
    st.markdown('<div id="team"></div>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #d2691e;'>Meet Our Team</h2>", unsafe_allow_html=True)

    html_code = """
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">

    <style>
    .team-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 30px;
        padding: 20px;
    }
    .card {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        width: 260px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    .card img {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        border: 3px solid #d2691e;
        object-fit: cover;
        margin-bottom: 15px;
    }
    .card h3 {
        margin: 10px 0 5px;
    }
    .card p.role {
        font-weight: 600;
        font-size: 14px;
        margin: 5px 0;
    }
    .card p.bio {
        font-size: 13px;
        color: #444;
        margin-bottom: 10px;
    }
    .social-icons {
        margin-top: 10px;
    }
    .social-icons a {
        margin: 0 6px;
        font-size: 18px;
        color: #333;
        text-decoration: none;
    }
    .social-icons a:hover {
        color: #d2691e;
    }
    </style>

    <div class="team-container">
        <div class="card">
            <img src="https://randomuser.me/api/portraits/men/10.jpg" alt="Balaji">
            <h3>Balaji R. Raparti</h3>
            <p class="role">Project Leader, Backend Developer</p>
            <p class="bio">Balaji's vision and leadership keep the team aligned and focused.</p>
            <div class="social-icons">
                <a href="#"><i class="fab fa-linkedin"></i></a>
                <a href="#"><i class="fab fa-instagram"></i></a>
                <a href="#"><i class="fab fa-facebook"></i></a>
            </div>
        </div>
        <div class="card">
            <img src="https://i.imgur.com/MmhBKy4.jpeg" alt="Amogh Waskar">
            <h3>Amogh J. Waskar</h3>
            <p class="role">Backend, Frontend Developer</p>
            <p class="bio">Amogh crafts seamless experiences across both front and back ends.</p>
            <div class="social-icons">
                <a href="#"><i class="fab fa-linkedin"></i></a>
                <a href="#"><i class="fab fa-instagram"></i></a>
                <a href="#"><i class="fab fa-facebook"></i></a>
            </div>
        </div>
        <div class="card">
            <img src="https://randomuser.me/api/portraits/men/25.jpg" alt="Jignesh Patil">
            <h3>Jignesh Patil</h3>
            <p class="role">Frontend Developer</p>
            <p class="bio">Jignesh ensures pixel-perfect design and responsive UI components.</p>
            <div class="social-icons">
                <a href="#"><i class="fab fa-linkedin"></i></a>
                <a href="#"><i class="fab fa-instagram"></i></a>
                <a href="#"><i class="fab fa-facebook"></i></a>
            </div>
        </div>
        <div class="card">
            <img src="https://randomuser.me/api/portraits/men/29.jpg" alt="Rohit Khobare">
            <h3>Rohit M. Khobare</h3>
            <p class="role">Frontend Developer, Coordinator</p>
            <p class="bio">Rohit handles smooth coordination and stunning interfaces.</p>
            <div class="social-icons">
                <a href="#"><i class="fab fa-linkedin"></i></a>
                <a href="#"><i class="fab fa-instagram"></i></a>
                <a href="#"><i class="fab fa-facebook"></i></a>
            </div>
        </div>
    </div>
    """

    components.html(html_code, height=850, scrolling=False)
