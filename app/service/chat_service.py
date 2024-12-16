from chain.agent import Agent

def chat_with_agent(user_input: str) -> str:
    agent = Agent()
    res = agent.get_agent().invoke(input = {'promble': user_input})
    # print(res.content)
    return res.content