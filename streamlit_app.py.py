import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="happpiieessttttttt birthdaaayyyy to myy DESIESTTTTTT POTLIIIIII!!!!!!", page_icon="❤️", layout="wide")

# 2. Maroon Theme & Glow CSS
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #4a0000 0%, #2b0000 100%);
        color: #ffffff;
    }
    
    .main-title {
        font-family: 'Georgia', serif;
        font-size: 60px !important;
        text-align: center;
        color: #ff4d4d;
        text-shadow: 0 0 15px #ff0000, 0 0 30px #800000;
        margin-bottom: 5px;
    }

    /* Glowing Borders for All Photos */
    .stImage > img {
        border: 3px solid #ff4d4d;
        border-radius: 15px;
        box-shadow: 0 0 15px #ff4d4d, 0 0 5px #ff4d4d;
        transition: transform 0.3s ease;
    }
    
    .stImage > img:hover {
        transform: scale(1.05);
        box-shadow: 0 0 25px #ff0000;
    }

    h3 {
        text-align: center;
        color: #ffb3b3;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Floating Balloons
st.balloons()

# 4. Header
st.markdown('<p class="main-title">Happy Birthday! ❤️</p>', unsafe_allow_html=True)
st.markdown("### To a very special person on their special day")
st.write("---")

# 5. The 5-Photo Grid
# Row 1: 3 Photos
col1, col2, col3 = st.columns(3)
with col1:
    st.image("avi1.jpeg")
with col2:
    st.image("avi5.jpeg")
with col3:
    st.image("avi6.jpeg")

# Row 2: 2 Photos (Centered)
# We use empty 'buffer' columns to keep the 2 photos in the middle
buf1, col4, col5, buf2 = st.columns([1, 2, 2, 1])
with col4:
    st.image("avi7.jpeg")
with col5:
    st.image("avi9.jpeg")

st.write("---")

# 6. Final Celebration Section
st.markdown("### 💌 My Birthday Message:")
st.info("Wishing you a year full of love, happiness, and all the things you enjoy most. You deserve the world!")

if st.button('Click for a Birthday Surprise! 🎆'):
    st.snow()
    st.balloons()
    st.success("Cheers to you! 🥂")
