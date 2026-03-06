import streamlit as st
import google.generativeai as genai
import os

# API Key check karne ka smart tarika
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ Bhai, API Key missing hai! Kripya Render ke 'Environment' setting mein GEMINI_API_KEY daalein.")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')

    st.title("🔥 The Khooni Agent - Viral Idea Generator")
    st.write("Ab kisi bhi niche mein viral content banao!")

    category = st.selectbox(
        "Video ki Category chuno:", 
        ["Gaming (BGMI/PUBG)", "Cartoon & Anime Story", "Comedy & Funny", "Tech & AI", "Dropshipping & Business", "Koi aur topic..."]
    )

    topic = st.text_input("Exact topic kya hai? (Jaise: BGMI update, AI tools, Tiger dog funny vlog):")

    system_prompt = f"""
    Tum ek World-Class YouTube Strategist aur Creative Director ho. 
    Mera channel multi-niche hai. Category: {category} aur specific topic: {topic} hai.

    Mujhe 3 specific sections mein idea do:
    1. THE VIRAL ANGLE: Ek unique story angle batao.
    2. THE CLICKABLE THUMBNAIL: Visual scene, background, aur text batao.
    3. EDITOR'S BLUEPRINT: Trending audio vibe aur editing style batao.
    Hinglish mein aur exciting tone mein jawab do.
    """

    if st.button("Idea Generate Karo"):
        if topic:
            with st.spinner("Khaufnak aur viral ideas soch raha hu..."):
                try:
                    response = model.generate_content(system_prompt)
                    st.success("Ye lo bhai, tumhara idea:")
                    st.write(response.text)
                except Exception as e:
                    st.error("Bhai AI connect hone mein dikkat aa rahi hai. Kya tumne Google API key sahi daali hai?")
        else:
            st.warning("Bhai pehle koi topic toh likh do!")

            
