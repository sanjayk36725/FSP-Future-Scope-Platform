"""Base AI Agent Class"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, List
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class BaseAgent(ABC):
    """Base class for all AI agents"""

    def __init__(self, agent_id: str, agent_name: str, description: str):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.description = description
        self.created_at = datetime.utcnow()

    @abstractmethod
    async def process_message(self, message: str, context: Dict[str, Any]) -> str:
        """Process user message and return AI response"""
        pass

    @abstractmethod
    async def process_file(self, file_path: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Process uploaded file"""
        pass

    async def get_agent_info(self) -> Dict[str, Any]:
        """Get agent information"""
        return {
            "agent_id": self.agent_id,
            "agent_name": self.agent_name,
            "description": self.description,
            "created_at": self.created_at.isoformat()
        }

    def log_interaction(self, user_message: str, ai_response: str):
        """Log agent interaction"""
        logger.info(
            f"Agent: {self.agent_name} | "
            f"User: {user_message[:50]}... | "
            f"Response: {ai_response[:50]}..."
        )
