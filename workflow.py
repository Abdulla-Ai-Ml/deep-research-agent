from langgraph.graph import Graph
from typing import TypedDict
from research_agent import ResearchAgent
from answer_drafter import AnswerDrafter

class ResearchState(TypedDict):
    query: str
    research: str
    answer: str

def setup_workflow():
    research_agent = ResearchAgent()
    answer_drafter = AnswerDrafter()
    
    workflow = Graph()
    
    workflow.add_node("research", lambda state: {
        "research": research_agent.research(state["query"])["output"]
    })
    
    workflow.add_node("draft_answer", lambda state: {
        "answer": answer_drafter.draft_answer(state["research"], state["query"])
    })
    
    workflow.set_entry_point("research")
    workflow.add_edge("research", "draft_answer")
    workflow.set_finish_point("draft_answer")
    
    return workflow.compile()