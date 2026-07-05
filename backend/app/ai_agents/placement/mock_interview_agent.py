"""Mock Interview Agent"""

from typing import Dict, Any
from app.ai_agents.base_agent import BaseAgent

class MockInterviewAgent(BaseAgent):
    """Mock Interview AI Agent"""

    def __init__(self):
        super().__init__(
            agent_id="mock_interview",
            agent_name="Mock Interview Agent",
            description="Conducts AI-based mock interviews and provides feedback"
        )

    async def process_message(self, message: str, context: Dict[str, Any]) -> str:
        """Conduct mock interview"""
        return f"Mock Interview Response to: {message[:50]}..."

    async def process_file(self, file_path: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Process interview materials"""
        return {"status": "success", "message": "Interview practice setup"}
