import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="HBD Special Someone", page_icon="❤️", layout="wide")

# 2. Custom CSS for Maroon Theme and Glowing Borders
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: radial-gradient(circle, #4a0000 0%, #2b0000 100%);
        color: #ffffff;
    }
    
    /* Glowing Title */
    .main-title {
        font-family: 'Georgia', serif;
        font-size: 65px !important;
        text-align: center;
        color: #ff4d4d;
        text-shadow: 0 0 15px #ff0000, 0 0 25px #800000;
        margin-bottom: 10px;
    }

    /* Glowing Image Borders */
    .stImage > img {
        border: 3px solid #ff4d4d;
        border-radius: 15px;
        box-shadow: 0 0 15px #ff4d4d, 0 0 5px #ff4d4d;
        transition: transform 0.4s ease;
    }
    
    .stImage > img:hover {
        transform: scale(1.08);
        box-shadow: 0 0 25px #ff0000, 0 0 15px #ff4d4d;
    }

    /* Styling the Expander/Vault */
    .streamlit-expanderHeader {
        background-color: #600000 !important;
        color: white !important;
        border-radius: 10px !important;
        font-size: 20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Floating Balloons
st.balloons()

# 4. Header Section
st.markdown('<p class="main-title">Happy Birthday! ❤️</p>', unsafe_allow_html=True)
st.write("<h4 style='text-align: center; color: #ffb3b3;'>A special day for a very special person.</h4>", unsafe_allow_html=True)

st.write("---")

# 5. The Main Gallery (3 Images)
st.write("### 🌹 Our Favorite Moments")
m_col1, m_col2, m_col3 = st.columns(3)

with m_col1:
    st.image("photo1.jpg", caption="The beginning ✨")

with m_col2:
    st.image("photo2.jpg", caption="Pure joy ❤️")

with m_col3:
    st.image("photo3.jpg", caption="Always you 🌹")

st.write("---")

# 6. The Surprise Vault (2 More Images)
with st.expander("🎁 CLICK TO UNLOCK THE FINAL SURPRISE"):
    st.write("#### I saved the best for last...")
    v_col1, v_col2 = st.columns(2)
    
    with v_col1:
        st.image("photo4.jpg", caption="Unforgettable.")
    
    with v_col2:
        st.image("photo5.jpg", caption="To many more years!")
        
    st.write("### You are truly one of a kind. Enjoy every second of your day! 🥂")
    if st.button("Click for Fireworks! 🎆"):
        st.snow()
        st.balloons()
