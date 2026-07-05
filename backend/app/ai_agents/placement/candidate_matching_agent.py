"""Candidate Matching Agent"""

from typing import Dict, Any
from app.ai_agents.base_agent import BaseAgent

class CandidateMatchingAgent(BaseAgent):
    """Candidate Matching AI Agent"""

    def __init__(self):
        super().__init__(
            agent_id="candidate_matching",
            agent_name="Candidate Matching Agent",
            description="Matches candidates to suitable job roles using skills"
        )

    async def process_message(self, message: str, context: Dict[str, Any]) -> str:
        """Match candidates to jobs"""
        return f"Candidate Matching Response to: {message[:50]}..."

    async def process_file(self, file_path: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Match candidate to jobs"""
        return {"status": "success", "message": "Matching completed"}
