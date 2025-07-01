from langchain.prompts import PromptTemplate
from langchain.agents import AgentExecutor, create_react_agent
from src.agent.core import config

def create_social_media_agent(tools: list) -> AgentExecutor:
    """
    Creates and returns a LangChain agent executor configured for social media tasks.

    Args:
        tools (list): A list of LangChain tools the agent can use.

    Returns:
        AgentExecutor: The configured agent ready to run.
    """
    # Use the singleton LLM client from config for the agent's "brain"
    llm = config.text_gen_llm

    # The prompt template remains the same, as it's a standard ReAct prompt.
    prompt = PromptTemplate.from_template("""
    You are a helpful social media assistant. Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times. This Thought/Action/Action Input/Observation should stop when you have successfully posted on social media or after 2 times.)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin!

    Question: {input}
    {agent_scratchpad}
    """)

    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors="Check your output and make sure it conforms to the format."
    )

    print("Social Media Agent created successfully.")
    return agent_executor