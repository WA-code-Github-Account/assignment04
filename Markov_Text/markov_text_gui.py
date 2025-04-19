import streamlit as st
import random

# 💠 Custom Page Config
st.set_page_config(page_title="Markov Chain Text Composer 🎶", page_icon="🎵", layout="centered")

# 💖 App Title and Subheading
st.markdown("""
    <div style='text-align: center; padding: 10px; background-color: #f9f9f9; border-radius: 12px;'>
        <h1 style='color:#6C63FF;'>🎶 Markov Chain Text Composer</h1>
        <h4 style='color:#555;'>By Aziza Siddiqui</h4>
        <p style='font-style: italic; color:#888;'>🎤 Let AI remix your lyrics using Markov Chain Magic!</p>
    </div>
""", unsafe_allow_html=True)

# 🧠 Function to build Markov Chain
def build_markov_chain(text):
    words = text.split()
    chain = {}
    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]
        if word not in chain:
            chain[word] = []
        chain[word].append(next_word)
    return chain

# 🎲 Function to generate lyrics
def generate_text(chain, length):
    if not chain:
        return ""
    word = random.choice(list(chain.keys()))
    result = [word]
    for _ in range(length - 1):
        next_words = chain.get(word, list(chain.keys()))
        word = random.choice(next_words)
        result.append(word)
    return ' '.join(result)

# 📝 Text input area with placeholder lyrics
user_input = st.text_area("🎧 Enter some lyrics or poetic lines:", 
"""Twinkle twinkle little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky""", height=150)

# 🔢 Word count slider
word_count = st.slider("🔢 Select number of words to generate:", min_value=10, max_value=100, value=20)

# 🚀 Generate button
if st.button("✨ Generate Magic Lyrics!"):
    chain = build_markov_chain(user_input)
    generated = generate_text(chain, word_count)

    st.markdown("---")
    st.markdown("### 🎼 AI-Generated Lyrics:")
    st.success(generated)
    st.markdown("---")

# 📌 Footer
st.markdown("""
    <div style='text-align: center; font-size: 13px; color: #aaa; padding-top: 20px;'>
        Made with ❤️ using Python & Streamlit | © Aziza Siddiqui
    </div>
""", unsafe_allow_html=True)
