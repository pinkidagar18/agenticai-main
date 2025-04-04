import openai
from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

import os 
import phi
from phi.playground import Playground, serve_playground_app
# load environment variable from .env file
load_dotenv()

phi.api_key=os.getenv("PHI_API_KEY")

##web search agent 
web_search_agent=Agent(
    name="Web search Agent",
    role="Search the web for the information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)


## Financial agent
dinance_agent=Agent(
    name="Finance AI Agent",
     model = Groq(id="llama-3.3-70b-versatile"),
    

    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                         company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tools_calls=True,
    markdown=True,      

)

app=Playground(agents=[dinance_agent,web_search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)