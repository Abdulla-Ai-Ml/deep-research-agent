from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

class ResearchAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4-turbo")
        self.tools = self._setup_tools()
        self.agent = self._create_agent()
    
    def _setup_tools(self):
        tavily_tool = TavilySearchResults(
            name="web_search",
            description="Search the web for up-to-date information"
        )
        return [tavily_tool]
    
    def _create_agent(self):
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a research assistant. Gather detailed and accurate information."),
            ("user", "{input}")
        ])
        agent = create_tool_calling_agent(self.llm, self.tools, prompt)
        return AgentExecutor(agent=agent, tools=self.tools)
    
    def research(self, query):
        return self.agent.invoke({"input": query})