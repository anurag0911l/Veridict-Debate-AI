import streamlit as st
import requests
import time

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Veridict",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- SESSION STATE ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode" not in st.session_state:
    st.session_state.mode = None

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
    radial-gradient(circle at top left, rgba(16,185,129,0.15), transparent 30%),
    radial-gradient(circle at top right, rgba(6,182,212,0.12), transparent 25%),
    linear-gradient(135deg, #020617 0%, #04120f 45%, #052e2b 100%);
    color: white;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container {
    padding-top: 1.5rem;
    max-width: 1400px;
}

.hero-title {
    text-align:center;
    font-size:78px;
    font-weight:900;
    line-height:1;
    margin-top:20px;
    color:#ecfdf5;
    letter-spacing:-3px;
}

.hero-subtitle {
    text-align:center;
    font-size:22px;
    color:#94a3b8;
    margin-top:15px;
    margin-bottom:60px;
}

.hero-highlight {
    color:#10b981;
}

.mode-card {
    background: rgba(15,23,42,0.72);
    border:1px solid rgba(16,185,129,0.18);
    border-radius:28px;
    padding:35px;
    min-height:260px;
    backdrop-filter: blur(20px);
    transition:0.3s ease;
    box-shadow:0 0 40px rgba(16,185,129,0.08);
}

.mode-card:hover {
    transform:translateY(-6px);
    border:1px solid rgba(16,185,129,0.45);
    box-shadow:0 0 60px rgba(16,185,129,0.16);
}

.mode-title {
    font-size:34px;
    font-weight:800;
    color:#ecfdf5;
    margin-bottom:15px;
}

.mode-desc {
    color:#94a3b8;
    font-size:18px;
    line-height:1.8;
}

.mode-tag {
    display:inline-block;
    padding:8px 16px;
    border-radius:999px;
    background:rgba(16,185,129,0.15);
    color:#6ee7b7;
    margin-top:18px;
    font-size:14px;
    font-weight:700;
}

.stButton > button {
    width:100%;
    height:60px;
    border:none;
    border-radius:18px;
    background:linear-gradient(90deg,#059669,#10b981);
    color:white;
    font-size:18px;
    font-weight:800;
    margin-top:15px;
    transition:0.25s ease;
    box-shadow:0 0 25px rgba(16,185,129,0.25);
}

.stButton > button:hover {
    transform:translateY(-2px);
    box-shadow:0 0 40px rgba(16,185,129,0.4);
}

.arena-header {
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:25px;
}

.arena-title {
    font-size:42px;
    font-weight:900;
    color:#ecfdf5;
}

.status-pill {
    padding:10px 18px;
    border-radius:999px;
    background:rgba(16,185,129,0.14);
    color:#6ee7b7;
    font-weight:700;
}

.chat-shell {
    background: rgba(15,23,42,0.7);
    border:1px solid rgba(16,185,129,0.18);
    border-radius:30px;
    padding:28px;
    min-height:68vh;
    backdrop-filter: blur(20px);
}

.user-bubble {
    background: linear-gradient(90deg,#047857,#059669);
    color:white;
    padding:18px 22px;
    border-radius:22px 22px 6px 22px;
    margin-left:auto;
    width:fit-content;
    max-width:72%;
    margin-bottom:18px;
    font-size:17px;
    line-height:1.7;
    box-shadow:0 0 20px rgba(16,185,129,0.18);
}

.ai-bubble {
    background:#0f172a;
    border:1px solid rgba(16,185,129,0.22);
    color:#e2e8f0;
    padding:20px 24px;
    border-radius:22px 22px 22px 6px;
    width:fit-content;
    max-width:75%;
    margin-bottom:18px;
    font-size:17px;
    line-height:1.9;
    box-shadow:0 0 25px rgba(16,185,129,0.08);
}

.sidebar-box {
    background: rgba(15,23,42,0.65);
    border:1px solid rgba(16,185,129,0.15);
    border-radius:24px;
    padding:22px;
    margin-bottom:20px;
}

.metric-title {
    color:#94a3b8;
    font-size:14px;
    margin-bottom:10px;
}

.metric-value {
    color:#ecfdf5;
    font-size:28px;
    font-weight:800;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LANDING PAGE ---------------- #

if st.session_state.mode is None:

    st.markdown(
        "<div class='hero-title'>⚔️ Debate <span class='hero-highlight'>AI</span></div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='hero-subtitle'>Truth emerges through the clash of intelligent ideas.</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.markdown("""
        <div class='mode-card'>
            <div class='mode-title'>👤 Human vs AI</div>
            <div class='mode-desc'>
                Challenge an advanced AI opponent in live real-time debate.
                Counter arguments, defend your logic, and test your reasoning.
            </div>
            <div class='mode-tag'>LIVE INTERACTIVE MODE</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Enter Human vs AI Arena"):
            st.session_state.mode = "human"
            st.rerun()

    with col2:

        st.markdown("""
        <div class='mode-card'>
            <div class='mode-title'>🤖 AI vs AI</div>
            <div class='mode-desc'>
                Watch two advanced AI minds battle each other using logic,
                rebuttals, persuasion, and strategic reasoning.
            </div>
            <div class='mode-tag'>COMING NEXT</div>
        </div>
        """, unsafe_allow_html=True)

        st.button("AI vs AI Coming Soon")

# ---------------- HUMAN VS AI ---------------- #

elif st.session_state.mode == "human":

    left, right = st.columns([4.5, 1.4], gap="large")

    with left:

        st.markdown("""
        <div class='arena-header'>
            <div class='arena-title'>👤 Human vs AI Debate Arena</div>
            <div class='status-pill'>● LIVE</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='chat-shell'>", unsafe_allow_html=True)

        if len(st.session_state.messages) == 0:

            st.markdown(
                """
                <div class='ai-bubble'>
                🤖 Welcome to Debate AI.<br><br>
                Present your first argument and I will challenge your reasoning in real time.
                </div>
                """,
                unsafe_allow_html=True
            )

        for msg in st.session_state.messages:

            if msg["role"] == "user":

                st.markdown(
                    f"""
                    <div style='display:flex; justify-content:flex-end;'>
                        <div class='user-bubble'>
                            👤 {msg['content']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div style='display:flex; justify-content:flex-start;'>
                        <div class='ai-bubble'>
                            🤖 {msg['content']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.markdown("</div>", unsafe_allow_html=True)

        user_input = st.chat_input("Present your argument...")

        if user_input:

            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })

            with st.spinner("AI is formulating rebuttal..."):

                response = requests.post(
                    "http://127.0.0.1:8000/chat",
                    json={
                        "messages": st.session_state.messages
                    }
                )

                data = response.json()

                ai_response = data.get(
                    "response",
                    "No response generated."
                )

                time.sleep(0.6)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": ai_response
                })

            st.rerun()

    with right:

        st.markdown(f"""
        <div class='sidebar-box'>
            <div class='metric-title'>Debate Messages</div>
            <div class='metric-value'>{len(st.session_state.messages)}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='sidebar-box'>
            <div class='metric-title'>AI Engine</div>
            <div class='metric-value'>Powered by ALPHA</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='sidebar-box'>
            <div class='metric-title'>Debate Status</div>
            <div class='metric-value'>ACTIVE</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🧹 Clear Debate"):
            st.session_state.messages = []
            st.rerun()

        if st.button("🏠 Return Home"):
            st.session_state.messages = []
            st.session_state.mode = None
            st.rerun()