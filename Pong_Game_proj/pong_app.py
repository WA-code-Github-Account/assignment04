

import streamlit as st


# App ka title aur layout set kar rahe hain
st.set_page_config(page_title="Aziza's Pong Game", layout="centered")
st.title("🎾 Pong Game - A.Siddiqui Style")

import streamlit as st

# --- Game State Initialization ---
if "ball_pos" not in st.session_state:
    st.session_state.ball_pos = 0
    st.session_state.score_a = 0
    st.session_state.score_b = 0
    st.session_state.message = "🎯 Game is ready. Start Playing!"

# --- Move Ball Function ---
def move_ball(direction):
    # Roman: Ball ko move karo left ya right
    if direction == "left":
        st.session_state.ball_pos -= 1
    elif direction == "right":
        st.session_state.ball_pos += 1

    # Roman: Score update karo agar ball end tak chali jaye
    if st.session_state.ball_pos <= -5:
        st.session_state.score_b += 1
        st.session_state.ball_pos = 0
        st.session_state.message = "🎉 Player B scores a point!"
    elif st.session_state.ball_pos >= 5:
        st.session_state.score_a += 1
        st.session_state.ball_pos = 0
        st.session_state.message = "🎉 Player A scores a point!"

# --- Display Ball Function ---
def display_ball():
    # Roman: Ball ki position show karo 11 boxes mein
    position = st.session_state.ball_pos + 5
    field = ["⬜"] * 11
    if 0 <= position < len(field):
        field[position] = "🔴"
    st.markdown(f"<div style='font-size:32px; text-align:center;'>{''.join(field)}</div>", unsafe_allow_html=True)

# --- 1. Game Status Message ---
st.subheader(st.session_state.message)

# --- 2. Ball Display (Top) ---
display_ball()

# --- Gap Between Ball and Buttons ---
st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)  # Roman: Gap add kiya

# --- 3. Movement Buttons ---
col1, col2 = st.columns(2)
with col1:
    if st.button("⬅️ Move Left"):
        move_ball("left")
with col2:
    if st.button("➡️ Move Right"):
        move_ball("right")

# --- 4. Score Display ---
st.markdown("---")
st.markdown("### 🧮 Scores")
score_col1, score_col2 = st.columns(2)
with score_col1:
    st.success(f"Player A: {st.session_state.score_a}")
with score_col2:
    st.info(f"Player B: {st.session_state.score_b}")

# --- 5. Reset Button (Bottom) ---
st.markdown("---")
if st.button("🔄 Reset Game"):
    st.session_state.score_a = 0
    st.session_state.score_b = 0
    st.session_state.ball_pos = 0
    st.session_state.message = "🎯 Game is reset. Start Again!"


