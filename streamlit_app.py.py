import streamlit as st

# 1. Page Setup
st.set_page_config(page_title="Happy Birthday!", page_icon="🌙", layout="wide")

# 2. Dark Theme & Glow CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        background-image: radial-gradient(circle at 50% 50%, #1a1a2e 0%, #0e1117 100%);
        color: #ffffff;
    }
    
    /* Glowing Title */
    .glow-text {
        font-size: 60px !important;
        font-weight: 800;
        text-align: center;
        color: #fff;
        text-shadow: 0 0 10px #00d4ff, 0 0 20px #00d4ff, 0 0 40px #00d4ff;
        padding: 20px;
    }

    /* Smaller, rounded photos with borders */
    .stImage > img {
        border-radius: 15px;
        border: 2px solid #3e3e3e;
        transition: transform 0.3s ease;
    }
    .stImage > img:hover {
        transform: scale(1.05);
        border-color: #00d4ff;
    }

    /* Custom Button Style */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background: linear-gradient(45deg, #00d4ff, #0055ff);
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Intro Surprise
st.balloons()
st.markdown('<p class="glow-text">HAPPY BIRTHDAY!</p>', unsafe_allow_html=True)

# 4. Main Photo Gallery (Smaller Sizes)
st.write("### 📸 Captured Moments")
col1, col2, col3 = st.columns(3) # Using 3 columns makes images smaller

with col1:
    st.image("photo1.jpg", use_container_width=True)
with col2:
    st.image("photo2.jpg", use_container_width=True)
with col3:
    st.image("photo3.jpg", use_container_width=True)

# 5. The "Secret Vault" Surprise
st.write("---")
st.write("### 🎁 There's something more...")

# This "Expander" acts as a hidden surprise
with st.expander("CLICK TO OPEN THE SECRET MEMORY VAULT 🔒"):
    st.write("#### You thought that was it? Here are some extra favorites!")
    
    # Grid for more photos
    v_col1, v_col2 = st.columns(2)
    with v_col1:
        st.image("photo4.jpg", caption="Throwback!", use_container_width=True)
    with v_col2:
        st.image("photo5.jpg", caption="The best day.", use_container_width=True)
    
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") # Optional: placeholder music link
    st.success("You're the best! 🥂")

# 6. Interactive Toast Surprise
if st.button('Click for a Birthday Toast! 🥂'):
    st.snow()
    st.confetti = True
    st.write("### 🥂 Cheers to you!")
    st.write("May your year be filled with success, laughter, and endless joy.")

