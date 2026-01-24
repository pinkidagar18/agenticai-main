# 📊 Financial AI Agent

> Real-time stock analysis powered by AI with a beautiful Streamlit interface

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-latest-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Overview

Financial AI Agent is a multi-agent system that provides real-time stock market data, analysis, and insights. Built with PhiData, Groq's LLM, and Streamlit, it offers an intuitive interface for financial research and stock analysis.

## ✨ Features

- 🤖 **Three Specialized AI Agents**
  - Multi Agent (Orchestrator)
  - Finance Agent (Stock Data)
  - Web Search Agent (Market News)

- 📊 **Real-Time Stock Data**
  - Current prices
  - Analyst recommendations
  - Company fundamentals
  - Financial news

- 🎨 **Beautiful UI**
  - Clean, modern design
  - Dark sidebar with gradient theme
  - Quick action buttons
  - Chat history
  - Responsive layout

- ⚡ **Quick Actions**
  - One-click stock analysis (AAPL, TSLA, NVDA, MSFT, GOOGL, AMZN)
  - Pre-built market queries
  - Example prompts

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API Key ([Get it free here](https://console.groq.com/keys))

### Installation

1. **Clone or download the repository**
   ```bash
   cd financial-ai-agent
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   
   # Activate it
   # Windows:
   .venv\Scripts\activate
   
   # Mac/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

6. **Open your browser**
   
   The app will automatically open at `http://localhost:8501`

## 📁 Project Structure

```
financial-ai-agent/
│
├── streamlit_app.py          # Main Streamlit UI application
├── agents.py                  # AI agent definitions and logic
├── playground.py              # PhiData playground (optional)
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (API keys)
└── README.md                 # This file
```

## 🎯 Usage

### Using the Streamlit Interface

1. **Select an Agent** (in sidebar):
   - 🎯 **Multi Agent** - Combines finance + web search
   - 💰 **Finance Agent** - Stock data only (recommended)
   - 🌐 **Web Agent** - Market news and research

2. **Quick Actions** (click any button):
   - 🍎 Apple
   - 🚗 Tesla
   - 🔌 NVIDIA
   - 💻 Microsoft
   - 🔍 Google
   - 📦 Amazon

3. **Or type your query**:
   ```
   What is the current price of Apple stock?
   Analyze Tesla stock
   Compare Microsoft and Google
   What are the best AI stocks?
   ```

### Example Queries

**Stock Prices:**
```
What is the current price of AAPL?
Get Tesla stock price
Show me NVIDIA stock data
```

**Analysis:**
```
Analyze Microsoft stock
NVDA fundamentals and metrics
Apple stock analyst recommendations
```

**Comparisons:**
```
Compare Tesla and Ford stocks
AAPL vs MSFT comparison
Best tech stocks comparison
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### Customizing Agents

Edit `agents.py` to customize agent behavior.

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| Framework | Streamlit |
| AI Agents | PhiData |
| LLM | Groq (Llama 3.3 70B) |
| Stock Data | YFinance |
| Web Search | DuckDuckGo |

## 🐛 Troubleshooting

### Common Issues

**Issue: ModuleNotFoundError**
```bash
pip install -r requirements.txt
```

**Issue: GROQ_API_KEY not found**
```bash
1. Create .env file
2. Add: GROQ_API_KEY=your_actual_key
3. Restart the app
```

**Issue: Rate limit reached**
```bash
Wait 24 hours or upgrade at https://console.groq.com
```

## 🚢 Deployment

### Streamlit Cloud (Free)

1. Push to GitHub
2. Go to share.streamlit.io
3. Connect repo
4. Add secret: GROQ_API_KEY
5. Deploy! 🚀

## 📝 License

MIT License - Free for personal and commercial use

## 🙏 Credits

- PhiData - Agent framework
- Groq - Fast LLM inference
- YFinance - Stock data
- Streamlit - Web framework

---

**Built with ❤️ for traders and investors**

*Happy Trading! 📈💰*