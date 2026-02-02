import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="HBD Superstar", page_icon="🌻", layout="wide")

# 2. Advanced CSS for Theme and Animations
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #4a0000 0%, #2b0000 100%);
        color: #ffffff;
    }
    
    .big-glow {
        font-family: 'Georgia', serif;
        font-size: 70px !important;
        text-align: center;
        color: #ffcc00;
        text-shadow: 0 0 20px #ffcc00, 0 0 40px #ffae00;
        padding: 40px 0px;
    }

    /* Centered Button Styling */
    div.stButton > button {
        display: block;
        margin: 0 auto;
        background: linear-gradient(45deg, #ffcc00, #ffae00);
        color: #4a0000 !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border-radius: 50px;
        padding: 12px 35px;
        border: 2px solid #ffffff;
        box-shadow: 0 0 15px rgba(255, 204, 0, 0.6);
    }

    /* Glowing Image Borders */
    .stImage > img {
        border: 4px solid #ffcc00;
        border-radius: 15px;
        box-shadow: 0 0 20px #ffcc00;
        transition: transform 0.3s;
    }
    .stImage > img:hover {
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Navigation Memory
if 'page' not in st.session_state:
    st.session_state.page = 1

def go_to_page(page_number):
    st.session_state.page = page_number

# --- PAGE 1: THE BIG OPENING ---
if st.session_state.page == 1:
    st.balloons()
    st.markdown('<p class="big-glow">ITS YOUR<br>SPECIAL DAY..</p>', unsafe_allow_html=True)
    
    # Centering the button
    _, col_btn, _ = st.columns([1, 2, 1])
    with col_btn:
        if st.button("OPEN YOUR GIFT 🎁"):
            go_to_page(2)
            st.rerun()

# --- PAGE 2: THE "SUP BABE" REVEAL ---
elif st.session_state.page == 2:
    st.write("<br><br>", unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 1, 1])
    with col_btn:
        if st.button("SUP BABE? 😉"):
            st.session_state.reveal_photos = True
    
    if st.session_state.get('reveal_photos', False):
        st.balloons() 
        st.snow() # Falling drizzle effect
        
        st.markdown('<p style="text-align:center; font-size:40px;">🌻🌻🌻🌻🌻🌻🌻</p>', unsafe_allow_html=True)
        
        # 5 Photos in a Single Row
        cols = st.columns(5)
        with cols[0]: st.image("avi1.jpeg")
        with cols[1]: st.image("avi5.jpeg")
        with cols[2]: st.image("avi6.jpeg")
        with cols[3]: st.image("avi7.jpeg")
        with cols[4]: st.image("avi9.jpeg")
        
        st.write("<br><br>", unsafe_allow_html=True)
        _, col_btn_next, _ = st.columns([1, 1, 1])
        with col_btn_next:
            if st.button("FOR YOU ❤️"):
                go_to_page(3)
                st.rerun()

# --- PAGE 3: THE HEARTFELT MESSAGE ---
elif st.session_state.page == 3:
    st.markdown('<p class="big-glow" style="font-size:45px !important;">A SPECIAL MESSAGE</p>', unsafe_allow_html=True)
    
    _, col_msg, _ = st.columns([1, 4, 1])
    with col_msg:
        st.markdown("""
        <div style="background-color: rgba(255, 204, 0, 0.1); padding: 30px; border-radius: 25px; border: 2px solid #ffcc00; text-align: center;">
            <h1 style="color: #ffcc00;">To My Favorite Person,</h1>
            <p style="font-size: 22px; color: #ffb3b3;">
                I wanted to make something as bright as your smile. 
                May your day be filled with sunflowers and endless joy. 
                You deserve the best birthday ever!
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    if st.button("START OVER 🔄"):
        st.session_state.reveal_photos = False
        go_to_page(1)
        st.rerun()
