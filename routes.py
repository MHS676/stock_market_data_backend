from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
import models, schemas
from database import get_db

router = APIRouter()

@router.get("/trade/", response_model=schemas.PaginatedTradeResponse)
def get_trades(
    db: Session = Depends(get_db),
    trade_code: Optional[str] = Query(None, description="Filter by trade code"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Number of items per page"),
):
    """
    Get trades with pagination and optional trade code filtering.
    """
    query = db.query(models.TradeData)

    if trade_code:
        query = query.filter(models.TradeData.trade_code == trade_code)

    total_count = query.count()
    trades = query.offset((page - 1) * limit).limit(limit).all()

    return {
        "total": total_count,
        "page": page,
        "limit": limit,
        "trades": trades, 
    }