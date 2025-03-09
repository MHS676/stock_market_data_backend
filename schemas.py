from pydantic import BaseModel, field_validator
from typing import List
from datetime import date


class TradeDataResponse(BaseModel):
    id: int
    trade_code: str
    date: str 
    high: float
    low: float
    open: float
    close: float
    volume: int  

    @field_validator("date", mode="before")
    @classmethod
    def convert_date(cls, v):
        """ Convert `date` object to string format `YYYY-MM-DD` """
        if isinstance(v, date):
            return v.strftime("%Y-%m-%d")
        return str(v) 

    @field_validator("volume", mode="before")
    @classmethod
    def convert_volume(cls, v):
        """ Convert '33,870' -> 33870 """
        if isinstance(v, str):
            return int(v.replace(",", ""))
        return v  

    class Config:
        from_attributes = True


class PaginatedTradeResponse(BaseModel):
    total: int
    page: int
    limit: int
    trades: List[TradeDataResponse]
