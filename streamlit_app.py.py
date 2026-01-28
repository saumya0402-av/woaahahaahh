import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="wide")

# 2. Custom Styling (The "Magic" part)
st.markdown("""
    <style>
    /* This changes the background color and font */
    .stApp {
        background: linear-gradient(135deg, #fce4ec 0%, #f3e5f5 100%);
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* This makes the titles pop */
    .birthday-title {
        font-size: 50px !important;
        font-weight: 800 !important;
        color: #d81b60 !important;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 0px;
    }
    
    /* This styles your photos */
    img {
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        transition: transform .2s;
    }
    img:hover {
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Floating Balloons
st.balloons()

# 4. Header
st.markdown('<p class="birthday-title">✨ Happy Birthday, Superstar! ✨</p>', unsafe_allow_html=True)
st.write("<h3 style='text-align: center; color: #8e24aa;'>To many more years of adventure!</h3>", unsafe_allow_html=True)

st.write("---")

# 5. The Photo Gallery
col1, col2 = st.columns(2)

with col1:
    # Make sure these names match your GitHub files!
    st.image("candidate photo.jpg", use_container_width=True)
    st.markdown("<p style='text-align: center; font-style: italic;'>The best times!</p>", unsafe_allow_html=True)

with col2:
    st.image("CONFIRMATION CARD.jpg", use_container_width=True)
    st.markdown("<p style='text-align: center; font-style: italic;'>Always smiling!</p>", unsafe_allow_html=True)

# 6. Heartfelt Message Section
st.write("---")
st.success("### 💌 My Message to You:\nYou aren't just a year older, you're a year better! I'm so lucky to have you in my life. Let's make this day unforgettable!")

# 7. Final Interactive Button
if st.button('Click for one last surprise!'):
    st.snow()
    st.balloons()
    st.toast("Yay! Have the best day ever! 🎉")




