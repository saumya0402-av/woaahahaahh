import streamlit as st
import time

# Basic Page Config
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂")

# Balloon trigger!
st.balloons()

# Header Section
st.title("🎂 Happiestttt Birthday, dessiestttt potliiiiii !")
st.subheader("To the one who madee myy lifeeee thee besttt by justtt beingg in ittt.")

# --- PHOTO SECTION ---
# Replace 'candidate photo.jpg' with the actual path to your photos
col1 = st.columns(2)

col1:
    st.image("candidate photo.jpg", caption="A favorite memory ❤️")

# --- HEARTFELT MESSAGE ---
st.write("---")
st.markdown("""
### My Wish for You:
I hope your day is filled with as much joy as you bring to everyone around you. 
May this year be your best one yet! 
""")

# Interactive button
if st.button('Click for a surprise!'):
    st.snow() # Adds a magical snow effect
    st.confetti = True

    st.success("You are loved! Enjoy your special day! 🥳")



