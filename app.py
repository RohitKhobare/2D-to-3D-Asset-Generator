import json
import requests
import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
#dataset, info = tfds.load('scicite',with_info=True)

def get(path:str):
    with open(path, "r") as p:
        return json.load(p)

path1 = get("./ani1.json")
path2 = get("./ani2.json")
path3 = get("./ani3.json")

st.set_page_config(page_title="PBL Project", page_icon=":tada:", layout="wide")

st.markdown(
    """
    <style>
    body {
        background-color: alice-blue;  /* Replace with your desired color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.header("Welcome to 2D to 3D Assets Generator :wave:")
    st.title("Bring Your 2D Designs to Life in 3D!")
    st.write("Instantly transform 2D images into fully-realized 3D assets with our AI-powered generator. Whether you're a game developer, artist, or designer, bring your concepts to life with just a few clicks—no 3D modeling skills required.")

with st.container():
    st.write("_______________________________________________")
    left_column, right_column = st.columns(2)

    with left_column :
        st.subheader(":thinking_face: What does the tool do?")
        st.write(" ")
        st.write(" ")
        st.markdown("""
        - 🧠 **Analyzes** 2D images (like concept sketches, sprites, or photos) 

        - 🧩 **Estimates** depth, shape, and structure using AI

        - 🎨 **Generates** 3D meshes with textures, lighting, and details 

        - 🚀 **Outputs** assets ready for games, animation, AR/VR  
        """)

    with right_column:
        st_lottie(path1, height=300, width=600, key="coding1")

with st.container():
    st.write("_______________________________________________")
    left_column, right_column = st.columns(2)

    with left_column :
        st_lottie(path2, height=300, width=600, key="coding2")

    with right_column:
        st.subheader(":thinking_face: Who uses the tool?")
        st.write(" ")
        st.write(" ")
        st.markdown("""
        - 🎮 **Game Developers** – Quickly prototype or generate game-ready assets

        - 🧑‍🎨 **3D Artists** – Use as a starting point for detailed modeling  

        - ✏️ **Designers & Illustrators** – Visualize 2D work in 3D effortlessly

        - 🌐 **AR/VR Creators** – Populate virtual worlds faster with ready assets  
        """)

with st.container():
    st.write("_______________________________________________")
    left_column, right_column = st.columns(2)

    with left_column :
        st.subheader(":thinking_face: Why it's useful?")
        st.write(" ")
        st.write(" ")
        st.markdown("""
        - ⏱️ **Saves time and effort** compared to manually modeling from scratch 

        - 🌉 **Bridges the gap** between 2D art and 3D content creation  

        - 🙌 **Makes 3D accessible** to people without technical 3D modeling skills  
        """)

    with right_column:
        st_lottie(path3, height=300, width=600, key="coding3")

with st.container():
    st.markdown(
        """
        <a href="WebpgMain.html" target="_blank">
            <button style="font-size:16px;padding:10px 20px;border-radius:8px;">Try the tool ↗</button>
        </a>
        """,
        unsafe_allow_html=True
    )

with st.container():
    st.write("_______________________________________________")
    import streamlit as st
    import streamlit.components.v1 as components

    st.markdown("<h2 style='text-align: center; color: #d2691e;'>Meet Our Team</h2>", unsafe_allow_html=True)

    html_code = """
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">

    <style>
    body {
        margin: 0;
        padding: 0;
        font-family: 'Poppins', sans-serif;
    }
    .team-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 30px;
        padding: 20px;
        box-sizing: border-box;
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

    components.html(html_code, height=750, scrolling=False)


