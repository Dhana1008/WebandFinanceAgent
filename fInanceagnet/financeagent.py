import streamlit as st
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv
from agno.storage.agent.sqlite import SqliteAgentStorage
from agno.tools.yfinance import YFinanceTools

# Load environment variables
load_dotenv()
api_key = os.getenv("groq_key")
os.environ["GROQ_API_KEY"] = api_key

# Creating the Web Agent
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Groq(api_key=api_key, id ="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools()],
    storage=SqliteAgentStorage(table_name="web_agent", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

# Creating the Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(api_key=api_key, id ="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Always use tables to display data"],
    storage=SqliteAgentStorage(table_name="finance_agent", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
)

# Combining both agents into an agent team
agent_team = Agent(
    team=[web_agent, finance_agent],
    name="Agent Team (Web+Finance)",
    model=Groq(api_key=api_key, id="llama-3.3-70b-versatile"),
    show_tool_calls=False,
    markdown=True,
)

# Streamlit UI for user interaction
st.title("Agent Team (Web + Finance)")
st.write("Interact with the combined Web and Finance Agent")

user_input = st.text_area("Enter your query:", "")

if st.button("Submit"):
    if user_input.strip():
        with st.spinner("Processing..."):
            response = agent_team.run(user_input)
            st.markdown(response.content)
    else:
        st.error("Please enter a query.")
