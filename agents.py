"""
Financial AI Agents Module
Exports agents for use in streamlit_app.py
"""

from phidata.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

load_dotenv()

def create_agents():
    """
    Create and return all agents
    Returns: (web_agent, finance_agent, multi_agent)
    """
    
    # Get API key
    api_key = os.getenv("GROQ_API_KEY")
    
    # Web Search Agent
    web_agent = Agent(
        name="Web Search Agent",
        role="Search the web for information",
        model=Groq(id="llama-3.3-70b-versatile", api_key=api_key),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tool_calls=False,
        markdown=True,
    )
    
    # Finance Agent
    finance_agent = Agent(
        name="Finance AI Agent",
        model=Groq(id="llama-3.3-70b-versatile", api_key=api_key),
        tools=[
            YFinanceTools(
                stock_price=True,
                analyst_recommendations=True,
                stock_fundamentals=True,
                company_news=True
            ),
        ],
        instructions=["Use tables to display the data", "Always provide current stock prices"],
        show_tool_calls=False,
        markdown=True,
    )
    
    # Multi Agent
    multi_agent = Agent(
        team=[finance_agent, web_agent],
        model=Groq(id="llama-3.3-70b-versatile", api_key=api_key),
        instructions=["Always include sources", "Use tables to display the data"],
        show_tool_calls=False,
        markdown=True,
    )
    
    return web_agent, finance_agent, multi_agent


# For direct testing
if __name__ == "__main__":
    print("Testing agents...")
    web, finance, multi = create_agents()
    print("✅ All agents created successfully!")
    print(f"- Web Agent: {web.name}")
    print(f"- Finance Agent: {finance.name}")
    print(f"- Multi Agent: {multi.name}")
