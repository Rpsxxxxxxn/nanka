from sqlalchemy import Column, Integer, String, Boolean

from database import Base, engine

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Item(Base):
    __tablename__ = "item"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Integer)
    
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)