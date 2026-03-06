import streamlit as st
import google.generativeai as genai
import os

# API Key yahan connect hogi
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-pro')

# Website ka design
st.title("🔥 The Khooni Agent - Viral Idea Generator")
st.write("Apna topic daalo aur magic dekho!")

topic = st.text_input("Kis topic par video banani hai? (e.g., BGMI 3.0 update, New Anime Story):")

# Tumhara Master Prompt
system_prompt = f"""
Tum ek World-Class YouTube Strategist aur Creative Director ho. 
Mera topic hai: {topic}

Mujhe 3 specific sections mein idea do:
1. THE VIRAL ANGLE: Ek unique aur suspenseful story angle batao.
2. THE CLICKABLE THUMBNAIL: Visual scene, background, aur text batao.
3. EDITOR'S BLUEPRINT: Trending audio vibe aur editing style (jaise glitch effects, fast pacing) batao.
Hinglish mein aur exciting tone mein jawab do.
"""

if st.button("Idea Generate Karo"):
    if topic:
        with st.spinner("Khaufnak ideas soch raha hu..."):
            response = model.generate_content(system_prompt)
            st.success("Ye lo bhai, tumhara idea:")
            st.write(response.text)
    else:
        st.error("Bhai pehle koi topic toh likh do!")
