import streamlit as st

# 1. Page Setup
st.set_page_config(page_title="Happy Birthday!", page_icon="🌻", layout="wide")

# 2. Maroon Background & Sunflower Yellow Glow CSS
st.markdown("""
    <style>
    /* Deep Maroon Background */
    .stApp {
        background: radial-gradient(circle, #4a0000 0%, #2b0000 100%);
        color: #ffffff;
    }
    
    /* Glowing Title */
    .sunshine-title {
        font-family: 'Georgia', serif;
        font-size: 55px !important;
        text-align: center;
        color: #ffcc00;
        text-shadow: 0 0 10px #ffcc00, 0 0 20px #e6ac00;
        margin-bottom: 10px;
    }

    /* Yellow Glowing Borders + Sunflower Emoji Placement */
    .photo-container {
        position: relative;
        display: inline-block;
        width: 100%;
    }

    .stImage > img {
        border: 4px solid #ffcc00; /* Yellow Border */
        border-radius: 15px;
        box-shadow: 0 0 20px #ffcc00, 0 0 10px #e6ac00; /* Yellow Glow */
        transition: transform 0.3s ease;
        object-fit: cover;
    }
    
    .stImage > img:hover {
        transform: scale(1.1);
        box-shadow: 0 0 35px #ffcc00;
    }

    /* Customizing the Caption */
    .stMarkdown p {
        color: #ffcc00;
        text-align: center;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Floating Balloons
st.balloons()

# 4. Header
st.markdown('<p class="sunshine-title">Happy Birthday! 🌻</p>', unsafe_allow_html=True)
st.write("<h3 style='text-align: center; color: #ffb3b3;'>To someone who brings sunshine even to the darkest rooms.</h3>", unsafe_allow_html=True)
st.write("---")

# 5. The Single Row Gallery (5 Images)
# We use 5 equal columns to fit them all in one row
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.image("avi1.jpeg", caption="🌻")
with col2:
    st.image("avi5.jpeg", caption="🌻")
with col3:
    st.image("avi6.jpeg", caption="🌻")
with col4:
    st.image("avi7.jpeg", caption="🌻")
with col5:
    st.image("avi9.jpeg", caption="🌻")

st.write("---")

# 6. Birthday Message
st.info("### 💌 My Brightest Wishes:\nMay your year be as bright and cheerful as a field of sunflowers. You are loved, celebrated, and cherished today and always!")

# 7. Final Interactive Surprise
if st.button('Click for a Sunny Surprise! ✨'):
    st.balloons()
    st.snow() # Looks like falling petals against the dark background
    st.toast("Stay golden! 💛")
