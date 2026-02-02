import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="A Special Journey", page_icon="🌻", layout="wide")

# 2. Custom CSS (Maroon Theme + Glowing Borders + Sunflower Animation)
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #4a0000 0%, #2b0000 100%);
        color: #ffffff;
    }
    
    /* Yellow Glowing Title */
    .glow-text {
        font-family: 'Georgia', serif;
        font-size: 50px;
        text-align: center;
        color: #ffcc00;
        text-shadow: 0 0 15px #ffcc00;
        margin-top: 50px;
    }

    /* Glowing Borders for Images */
    .stImage > img {
        border: 4px solid #ffcc00;
        border-radius: 15px;
        box-shadow: 0 0 20px #ffcc00;
    }

    /* Centralized Button Style */
    div.stButton > button {
        display: block;
        margin: 0 auto;
        background-color: #ffcc00;
        color: #4a0000;
        font-weight: bold;
        border-radius: 20px;
        padding: 10px 25px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Initialize the "Page Tracker"
if 'page' not in st.session_state:
    st.session_state.page = 1

def go_to_page(page_number):
    st.session_state.page = page_number

# --- PAGE 1: THE INTRO ---
if st.session_state.page == 1:
    st.markdown('<p class="glow-text">It\'s Your Special Day...</p>', unsafe_allow_html=True)
    st.write("<br><br>", unsafe_allow_html=True)
    if st.button("Open Your Gift 🎁"):
        go_to_page(2)
        st.rerun()

# --- PAGE 2: THE SURPRISE REVEAL ---
elif st.session_state.page == 2:
    st.write("<br><br>", unsafe_allow_html=True)
    if st.button("Sup Babe? 😉"):
        st.session_state.reveal_photos = True
    
    if st.session_state.get('reveal_photos', False):
        # Trigger Sunflower "Drizzle" (Using Snowflakes logic but themed)
        st.snow() 
        st.markdown('<p class="glow-text">🌻 You Radiate Sunshine 🌻</p>', unsafe_allow_html=True)
        
        # All 5 photos in a single row
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1: st.image("avi1.jpeg")
        with col2: st.image("avi5.jpeg")
        with col3: st.image("avi6.jpeg")
        with col4: st.image("avi7.jpeg")
        with col5: st.image("avi9.jpeg")
        
        st.write("<br>", unsafe_allow_html=True)
        if st.button("For You ❤️"):
            go_to_page(3)
            st.rerun()

# --- PAGE 3: THE MESSAGE ---
elif st.session_state.page == 3:
    st.markdown('<p class="glow-text">My Heartfelt Wish</p>', unsafe_allow_html=True)
    
    # Message Box
    st.write("---")
    st.markdown("""
    <div style="background-color: rgba(255, 204, 0, 0.1); padding: 30px; border-radius: 20px; border: 1px solid #ffcc00; text-align: center;">
        <h2 style="color: #ffcc00;">To My Favorite Person,</h2>
        <p style="font-size: 20px; line-height: 1.6;">
            I wanted to create something as unique and bright as you are. 
            May your year be filled with the same warmth you give to everyone around you. 
            Happy Birthday, and I hope you loved this little surprise!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Start Over 🔄"):
        st.session_state.reveal_photos = False
        go_to_page(1)
        st.rerun()
