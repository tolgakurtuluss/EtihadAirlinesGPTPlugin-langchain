## !pip install langchain openai

# Import Statements
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.tools import AIPluginTool

# Define API key securely (using environment variable)
import os
openai_api_key = os.environ.get('OPENAI_API_KEY')

def initialize_chat_agent():
    # Load language model
    chat_model = ChatOpenAI(openai_api_key=openai_api_key, temperature=0)

    # Load required tools
    tool = AIPluginTool.from_plugin_url("https://gpt-etihad.botim.me/.well-known/ai-plugin.json")
    tools = load_tools(["requests_all"]) + [tool]

    # Initialize chat agent chain
    agent_chain = initialize_agent(tools, chat_model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    return agent_chain

def main():
    # Initialize the chat agent
    agent_chain = initialize_chat_agent()

    # Run the chat agent with a sample query
    query = "Search flights from IST to AUH on 1st of August 2023"
    agent_chain.run(query)

if __name__ == "__main__":
    main()
