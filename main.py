from workflow import setup_workflow
from dotenv import load_dotenv
import os

load_dotenv()

class DeepResearchSystem:
    def __init__(self):
        self.workflow = setup_workflow()
    
    def research(self, query):
        result = self.workflow.invoke({"query": query})
        return result["answer"]

if __name__ == "__main__":
    system = DeepResearchSystem()
    query = input("Enter your research query: ")
    answer = system.research(query)
    print("\n--- Final Answer ---")
    print(answer)