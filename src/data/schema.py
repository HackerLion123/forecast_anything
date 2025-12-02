from pydantic import BaseModel, Field



class NewsFeatures(BaseModel):
    """Schema for LLM-extracted news features."""
    sentiment_score: float = Field(description="Sentiment score from -1 (negative) to 1 (positive)")
    supply_chain_risk: float = Field(description="Supply chain disruption risk score from 0 to 1")
    demand_indicator: float = Field(description="Demand strength indicator from 0 to 1")
    price_pressure: float = Field(description="Price pressure score from -1 (downward) to 1 (upward)")
    market_volatility: float = Field(description="Market volatility indicator from 0 to 1")
    key_events: List[str] = Field(description="List of key events mentioned")