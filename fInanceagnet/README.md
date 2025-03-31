# Finance and Web Agent Chatbot

This project is a **Finance and Web Agent Chatbot** built using Python, Streamlit, and the Agno framework. The chatbot combines two agents:
1. **Web Agent**: Searches the web for general information.
2. **Finance Agent**: Retrieves financial data, including stock prices, analyst recommendations, company information, and news.

The agents are combined into a team to provide a seamless user experience for both web and financial queries.

## Features

### Web Agent
- Searches the web for general information using DuckDuckGo.
- Provides concise and accurate responses.

### Finance Agent
- Retrieves **stock prices** for companies.
- Provides **analyst recommendations** for stocks.
- Fetches **company information** and **news**.
- Displays financial data in **table format** for better readability.

### Combined Agent Team
- Handles both web and financial queries.
- Automatically routes queries to the appropriate agent.

## Prerequisites

- Python 3.10 or higher
- Required Python packages (install using `pip`):
  - `streamlit`
  - `agno`
  - `python-dotenv`

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/finance-web-agent.git
   cd finance-web-agent

2. **Run command**:
streamlit run [financeagent.py]