"""Payroll Support Agent"""

from typing import Dict, Any
from app.ai_agents.base_agent import BaseAgent

class PayrollSupportAgent(BaseAgent):
    """Payroll Support AI Agent"""

    def __init__(self):
        super().__init__(
            agent_id="payroll",
            agent_name="Payroll Support Agent",
            description="Provides salary, payslip, and payroll-related information"
        )

    async def process_message(self, message: str, context: Dict[str, Any]) -> str:
        """Provide payroll information"""
        return f"Payroll Support Response to: {message[:50]}..."

    async def process_file(self, file_path: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Process payroll documents"""
        return {"status": "success", "message": "Payroll information retrieved"}
