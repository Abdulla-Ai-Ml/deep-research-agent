from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

class AnswerDrafter:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4-turbo")
        self.chain = self._setup_chain()
    
    def _setup_chain(self):
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an answer drafting assistant. Summarize the research clearly and concisely. Include sources if available."""),
            ("user", "Research: {research}\n\nQuestion: {query}")
        ])
        return prompt | self.llm | StrOutputParser()
    
    def draft_answer(self, research, query):
        return self.chain.invoke({"research": research, "query": query})