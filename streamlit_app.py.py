import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="HBD Superstar", page_icon="🌻", layout="wide")

# 2. Advanced CSS for Centering and Glow
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #4a0000 0%, #2b0000 100%);
        color: #ffffff;
    }
    
    /* Extra Large Glowing Titles */
    .big-glow {
        font-family: 'Georgia', serif;
        font-size: 80px !important;
        text-align: center;
        color: #ffcc00;
        text-shadow: 0 0 20px #ffcc00, 0 0 40px #ffae00;
        padding: 50px 0px;
    }

    /* Centered Button Styling */
    div.stButton > button {
        display: block;
        margin: 0 auto;
        background: linear-gradient(45deg, #ffcc00, #ffae00);
        color: #4a0000 !important;
        font-size: 24px !important;
        font-weight: bold !important;
        border-radius: 50px;
        padding: 15px 40px;
        border: 2px solid #ffffff;
        box-shadow: 0 0 15px rgba(255, 204, 0, 0.5);
    }

    /* Glowing Image Borders */
    .stImage > img {
        border: 4px solid #ffcc00;
        border-radius: 20px;
        box-shadow: 0 0 25px #ffcc00;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State for Navigation
if 'page' not in st.session_state:
    st.session_state.page = 1

def go_to_page(page_number):
    st.session_state.page = page_number

# --- PAGE 1: THE BIG OPENING ---
if st.session_state.page == 1:
    st.balloons() # Popping up immediately
    st.markdown('<p class="big-glow">ITS YOUR<br>SPECIAL DAY..</p>', unsafe_allow_html=True)
    
    # Using columns to force the button to the absolute center
    col_l, col_btn, col_r = st.columns([1, 2, 1])
    with col_btn:
        if st.button("OPEN YOUR GIFT 🎁"):
            go_to_page(2)
            st.rerun()

# --- PAGE 2: THE "SUP BABE" REVEAL ---
elif st.session_state.page == 2:
    st.write("<br><br><br>", unsafe_allow_html=True)
    
    # Centered "Sup Babe" Button
    col_l, col_btn, col_r = st.columns([1, 1, 1])
    with col_btn:
        if st.button("SUP BABE? 😉"):
            st.session_state.reveal_photos = True
    
    if st.session_state.get('reveal_photos', False):
        # The Drizzle Effect (Balloons + Snow + Sunflowers)
        st.balloons() 
        st.snow()
        st.toast("SURPRISE! 🌻✨")
        
        st.markdown('<p style="text-align:center; font-size:40px;">🌻🌻🌻🌻🌻🌻🌻</p>', unsafe_allow_html=True)
        
        # 5 Photos in a Single Row
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.image(f"photo{i+1}.jpg", use_container_width=True)
        
        st.write("<br><br>", unsafe_allow_html=True)
        # Centered "For You" Button
        col_l, col_btn, col_r = st.columns([1, 1, 1])
        with col_btn:
            if st.button("FOR YOU ❤️"):
                go_to_page(3)
                st.rerun()

# --- PAGE 3: THE HEARTFELT MESSAGE ---
elif st.session_state.page == 3:
    st.markdown('<p class="big-glow" style="font-size:50px !important;">MY WISH FOR YOU</p>', unsafe_allow_html=True)
    
    col_l, col_msg, col_r = st.columns([1, 3, 1])
    with col_msg:
        st.markdown("""
        <div style="background-color: rgba(255, 204, 0, 0.1); padding: 40px; border-radius: 30px; border: 2px solid #ffcc00; text-align: center;">
            <h1 style="color: #ffcc00;">Dear [Name],</h1>
            <p style="font-size: 24px; line-height: 1.8; color: #ffb3b3;">
                Happy Birthday! You are the most incredible person I know. 
                May your day be filled with sunflowers, laughter, and all the love 
                you deserve. I hope this little digital gift made you smile!
            </p>
            <h2 style="color: #ffcc00;">✨ Stay Golden! ✨</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    if st.button("START OVER 🔄"):
        st.session_state.reveal_photos = False
        go_to_page(1)
        st.rerun()
