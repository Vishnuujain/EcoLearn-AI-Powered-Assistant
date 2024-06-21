from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    age = Column(Integer)
    interest_level = Column(String)
    learning_path = relationship("LearningPath", back_populates="user")

class LearningPath(Base):
    __tablename__ = "learning_paths"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user_profiles.id"))
    current_topic = Column(String)
    progress = Column(Integer)
    user = relationship("UserProfile", back_populates="learning_path")

    def update_progress(self, user_input, response):
        # Logic to update progress based on user interaction
        pass
