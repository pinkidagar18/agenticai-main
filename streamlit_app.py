import streamlit as st
from agents import create_agents  # Import from agents.py
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Financial AI Agent", page_icon="📊", layout="wide")

# Custom CSS - WHITE TEXT FOR RADIO BUTTONS
st.markdown("""
    <style>
    .main { background-color: #f5f7fa; }
    
    h1 {
        color: #1e3a8a;
        font-size: 3rem !important;
        font-weight: 700 !important;
    }
    
    .subtitle {
        color: #64748b;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e2e8f0;
        padding: 12px;
        font-size: 16px;
    }
    
    .stButton > button {
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: 600;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    .response-box {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
        margin-top: 1rem;
    }
    
    [data-testid="stSidebar"] {
        background-color: #1e293b;
        padding: 2rem 1rem;
    }
    
    [data-testid="stSidebar"] h2 {
        color: white !important;
        font-size: 1.5rem;
    }
    
    /* MAKE ALL RADIO BUTTON TEXT WHITE AND BOLD */
    [data-testid="stSidebar"] .stRadio label {
        color: white !important;
        font-weight: 700 !important;
        font-size: 16px !important;
    }
    
    [data-testid="stSidebar"] .stRadio > label {
        color: white !important;
        font-weight: 700 !important;
    }
    
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label {
        color: white !important;
        font-weight: 700 !important;
    }
    
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label > div {
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label span {
        color: white !important;
        font-weight: 700 !important;
    }
    
    [data-testid="stSidebar"] .stRadio p {
        color: white !important;
        font-weight: 700 !important;
    }
    
    [data-testid="stSidebar"] .stButton > button {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 0.5rem;
        width: 100%;
    }
    
    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateX(5px);
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("⚠️ Please add GROQ_API_KEY to your .env file")
    st.stop()

# Use agents from agents.py file
web_agent, finance_agent, multi_agent = create_agents()

with st.sidebar:
    st.markdown("## ⚙️ Settings")
    
    agent_choice = st.radio(
        "Select Agent:",
        ["🎯 Multi Agent", "💰 Finance Agent", "🌐 Web Agent"]
    )
    
    st.markdown("---")
    st.markdown("## 📈 Quick Actions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🍎 Apple", use_container_width=True):
            st.session_state.quick_query = "What is the current price of Apple (AAPL) stock?"
        if st.button("🚗 Tesla", use_container_width=True):
            st.session_state.quick_query = "What is the current price of Tesla (TSLA) stock?"
        if st.button("🔌 NVIDIA", use_container_width=True):
            st.session_state.quick_query = "What is the current price of NVIDIA (NVDA) stock?"
    
    with col2:
        if st.button("💻 Microsoft", use_container_width=True):
            st.session_state.quick_query = "What is the current price of Microsoft (MSFT) stock?"
        if st.button("🔍 Google", use_container_width=True):
            st.session_state.quick_query = "What is the current price of Google (GOOGL) stock?"
        if st.button("📦 Amazon", use_container_width=True):
            st.session_state.quick_query = "What is the current price of Amazon (AMZN) stock?"
    
    st.markdown("---")
    st.markdown("## 💡 Example Queries")
    
    if st.button("📊 Market Overview", use_container_width=True):
        st.session_state.quick_query = "What's happening in the stock market today?"
    if st.button("🔥 NVDA Analysis", use_container_width=True):
        st.session_state.quick_query = "What is the current price of NVDA?"
    if st.button("⚡ Tech Stocks", use_container_width=True):
        st.session_state.quick_query = "Get prices for AAPL, MSFT, GOOGL"
    
    st.markdown("---")
    if st.button("🗑️ Clear History", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

st.title("📊 Financial AI Agent")
st.markdown('<p class="subtitle">Get real-time stock data and market insights powered by AI</p>', unsafe_allow_html=True)

col_input, col_button = st.columns([4, 1])

with col_input:
    default_query = st.session_state.pop('quick_query', "")
    user_query = st.text_input("Enter your query", placeholder="e.g., What is the price of Apple stock?", value=default_query, label_visibility="collapsed")

with col_button:
    st.markdown("<br>", unsafe_allow_html=True)
    analyze_button = st.button("🔍 Analyze", use_container_width=True, type="primary")

if analyze_button and user_query:
    if agent_choice == "🎯 Multi Agent":
        selected_agent = multi_agent
    elif agent_choice == "💰 Finance Agent":
        selected_agent = finance_agent
    else:
        selected_agent = web_agent
    
    with st.spinner("🤔 Analyzing..."):
        try:
            response = selected_agent.run(user_query)
            st.session_state.chat_history.append({"query": user_query, "response": response.content, "agent": agent_choice})
        except Exception as e:
            error_str = str(e)
            if "rate_limit" in error_str.lower() or "429" in error_str:
                st.error("⚠️ Rate Limit Reached! Wait 24 hours or upgrade at https://console.groq.com")
            else:
                st.error(f"❌ Error: {error_str}")

if st.session_state.chat_history:
    latest = st.session_state.chat_history[-1]
    st.markdown("### 💬 Response:")
    st.markdown(f'<div class="response-box">{latest["response"]}</div>', unsafe_allow_html=True)
    
    if len(st.session_state.chat_history) > 1:
        with st.expander(f"📜 History ({len(st.session_state.chat_history)-1})"):
            for i, item in enumerate(reversed(st.session_state.chat_history[:-1])):
                st.markdown(f"**Q:** {item['query']}")
                st.markdown(f"**Agent:** {item['agent']}")
                st.markdown(item['response'])
                st.markdown("---")

if not st.session_state.chat_history:
    st.info("👋 Welcome! Click a stock button or enter your query above.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**📊 Stock Prices**\n- Apple price?\n- Tesla data?\n- NVIDIA info?")
    with col2:
        st.markdown("**📈 Analysis**\n- Analyze Microsoft\n- NVDA fundamentals\n- Compare stocks")
    with col3:
        st.markdown("**💰 Market**\n- Tech news\n- Best AI stocks\n- Market trends")

st.markdown("---")
st.markdown('<div style="text-align: center; color: #64748b;"><p>Powered by Groq AI • YFinance • DuckDuckGo</p></div>', unsafe_allow_html=True)