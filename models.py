from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TradeData(Base):
    __tablename__ = 'trade_data'
    
    
    date = Column(String, nullable=False)
    trade_code = Column(String, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    open = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(String, nullable=False)
    id = Column(Integer, primary_key=True, index=True)