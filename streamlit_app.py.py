import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="HBD Superstar", page_icon="🌻", layout="wide")

# 2. Advanced CSS for Theme, Animations, and Background Sparkles
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
        transition: transform 0.2s;
    }
    
    div.stButton > button:hover {
        transform: scale(1.1);
        box-shadow: 0 0 25px #ffcc00;
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

# --- GLOBAL CELEBRATION ---
st.balloons() 
st.snow()     

# 3. Navigation Memory
if 'page' not in st.session_state:
    st.session_state.page = 1

def go_to_page(page_number):
    st.session_state.page = page_number

# --- PAGE 1: THE BIG OPENING ---
if st.session_state.page == 1:
    st.markdown('<p class="big-glow">ITS YOUR DAYY GURRLLL 🤤🤤🤤🤤🤤🤤🫦🫦🫦🫦🫦🫦..</p>', unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 2, 1])
    with col_btn:
        if st.button("OPEN YOUR GIFT 🎁"):
            go_to_page(2)
            st.rerun()

# --- PAGE 2: THE "SUP BABE" REVEAL ---
elif st.session_state.page == 2:
    st.write("<br><br>", unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 2, 1])
    with col_btn:
        if st.button("HAPPIESTTT BIRTHDAYYYY DESIIESTTT POTLIIIII 🥹🥹🫶🏻🫶🏻"):
            st.session_state.reveal_photos = True
    
    if st.session_state.get('reveal_photos', False):
        st.markdown('<p style="text-align:center; font-size:40px;">🌻🌻🌻AAYYYYY HAAYYYEEEEEE🌻🌻🌻</p>', unsafe_allow_html=True)
        
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
    st.markdown('<p class="big-glow" style="font-size:45px !important;">FOR YOU</p>', unsafe_allow_html=True)
    
    # Hero Image for the final page
    _, col_hero, _ = st.columns([1, 2, 1])
    with col_hero:
        # REPLACE "hero_image.jpeg" with your final photo filename
        st.image("LOL.jpeg", use_container_width=True)
    
    st.write("<br>", unsafe_allow_html=True)

    _, col_msg, _ = st.columns([1, 4, 1])
    with col_msg:
        st.markdown("""
        <div style="background-color: rgba(255, 204, 0, 0.1); padding: 30px; border-radius: 25px; border: 2px solid #ffcc00; text-align: center;">
            <h1 style="color: #ffcc00;">To My Favorite Person, <br>BEING THE ONLY HABIT I NEVER WANNA BREAK,</h1>
            <p style="font-size: 20px; color: #ffb3b3; line-height: 1.6;">
                AAVVVVIISSHHAAA BBAABBBYYYYYYYYYYYYYY!!!!!!!! <br><br>
                HAAPPPPPPYYYYYYYYYY BIRTHHDDAAYYYYYYYYYYYYYYY DARLINNGGG <br>
                Thankyou so much for being the only dessiiii potlii to ever exist in my life
                being the hottest in our whole bloodline, SLAYING everywhere u go <br><br>
                Making ur own cousin question himself ke <i>"bhenchooddd annooo bhaii ajj kem banayoooo 
                parn koy othoo naiii"</i>. <br><br>
                Being the only person in my life jena jode bc 2 min na kam thi call kryo hoye and ends up on call for straight 3 HRS. <br><br>
                Hope you earn some real good shit and gift me reall cooll shiittt <br>
                YOU GOOOO GUURRLLLLLLLLLLL!!!!!! KEEP SLAYINNGGGGGGGG BICHHHH!! <br>
                <b>TO ANOTHER YEAR OF BEING THE BEST PART OF EVERYONE'S DAY</b>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    
    # Centered Start Over Button
    _, col_reset, _ = st.columns([1, 1, 1])
    with col_reset:
        if st.button("START OVER 🔄"):
            st.session_state.reveal_photos = False
            go_to_page(1)
            st.rerun()


