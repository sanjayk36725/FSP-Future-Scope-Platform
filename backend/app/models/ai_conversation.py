"""AI Conversation Models"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base

class AIConversation(Base):
    """AI Conversation Session Model"""
    __tablename__ = "ai_conversation"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
    agent_type = Column(String(100), nullable=False)  # Type of AI agent
    agent_name = Column(String(255))
    
    title = Column(String(500), nullable=True)
    context = Column(JSON, default={})
    
    total_messages = Column(Integer, default=0)
    total_tokens_used = Column(Integer, default=0)
    
    is_active = Column(String(50), default="yes")
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="ai_conversations")
    messages = relationship("AIMessage", back_populates="conversation", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<AIConversation {self.agent_type}>"

class AIMessage(Base):
    """AI Message in Conversation Model"""
    __tablename__ = "ai_message"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey('ai_conversation.id'), nullable=False)
    
    role = Column(String(50), nullable=False)  # user, assistant
    content = Column(Text, nullable=False)
    
    tokens_used = Column(Integer, default=0)
    
    metadata = Column(JSON, default={})
    
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    conversation = relationship("AIConversation", back_populates="messages")

    def __repr__(self):
        return f"<AIMessage {self.role}>"
