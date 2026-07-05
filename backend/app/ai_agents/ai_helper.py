"""AI Helper - Routes messages to appropriate agents"""

from typing import Dict, Any, Optional
import logging

from app.ai_agents.base_agent import BaseAgent
from app.ai_agents.education.personal_tutor_agent import PersonalTutorAgent
from app.ai_agents.education.coding_mentor_agent import CodingMentorAgent
from app.ai_agents.placement.resume_review_agent import ResumeReviewAgent
from app.ai_agents.development.code_review_agent import CodeReviewAgent

logger = logging.getLogger(__name__)

class AIHelper:
    """AI Helper - Central routing to AI agents"""

    def __init__(self):
        self.agents: Dict[str, BaseAgent] = {}
        self._initialize_agents()

    def _initialize_agents(self):
        """Initialize all available AI agents"""
        # Education Agents
        self.agents["personal_tutor"] = PersonalTutorAgent()
        self.agents["coding_mentor"] = CodingMentorAgent()
        
        # Placement Agents
        self.agents["resume_review"] = ResumeReviewAgent()
        
        # Development Agents
        self.agents["code_review"] = CodeReviewAgent()
        
        logger.info(f"Initialized {len(self.agents)} AI agents")

    async def route_to_agent(self, user_message: str, agent_type: str, context: Dict[str, Any]) -> str:
        """Automatically route message to appropriate AI agent"""
        agent = self.agents.get(agent_type)
        
        if not agent:
            return f"Agent '{agent_type}' not found. Available agents: {list(self.agents.keys())}"
        
        try:
            response = await agent.process_message(user_message, context)
            agent.log_interaction(user_message, response)
            return response
        except Exception as e:
            logger.error(f"Agent error: {str(e)}", exc_info=True)
            return f"Error processing request: {str(e)}"

    async def process_file_with_agent(self, file_path: str, agent_type: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Process file with appropriate agent"""
        agent = self.agents.get(agent_type)
        
        if not agent:
            return {"status": "error", "message": f"Agent '{agent_type}' not found"}
        
        try:
            result = await agent.process_file(file_path, context)
            return result
        except Exception as e:
            logger.error(f"Agent file processing error: {str(e)}", exc_info=True)
            return {"status": "error", "message": str(e)}

    def get_available_agents(self) -> list:
        """Get list of available agents"""
        return [
            {
                "id": agent_id,
                "name": agent.agent_name,
                "description": agent.description
            }
            for agent_id, agent in self.agents.items()
        ]

    def detect_agent_from_message(self, message: str) -> str:
        """Detect appropriate agent from user message"""
        message_lower = message.lower()
        
        # Keywords for different agents
        if any(word in message_lower for word in ["resume", "cv", "portfolio"]):
            return "resume_review"
        elif any(word in message_lower for word in ["code", "review", "github"]):
            return "code_review"
        elif any(word in message_lower for word in ["learn", "study", "explain", "understand"]):
            return "personal_tutor"
        elif any(word in message_lower for word in ["coding", "programming", "python", "java"]):
            return "coding_mentor"
        else:
            return "personal_tutor"  # Default agent
