import pandas as pd
import numpy as np
from typing import List, Dict, Optional
import logging
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser

from datetime import datetime

logger = logging.getLogger(__name__)




class LLMFeatureExtractor:
    """Extract features from time series data using LLM-generated insights."""
    
    def __init__(self, model_name: str = "gpt-3.5-turbo", domain: str = "general"):
        """
        Initialize the LLM feature extractor.
        
        Args:
            model_name: Name of the LLM model to use
            domain: Domain context (e.g., 'raw_materials', 'retail', 'energy')
        """
        self.model_name = model_name
        self.domain = domain
        self.llm = ChatOpenAI(model=model_name, temperature=0)
        self.parser = PydanticOutputParser(pydantic_object=NewsFeatures)
        
    def _get_domain_context(self) -> str:
        """Get domain-specific context for the LLM."""
        contexts = {
            "raw_materials": """Focus on commodity prices, supply chain disruptions, 
            geopolitical events affecting mining/extraction, weather impacts on production,
            trade policies, and inventory levels.""",
            
            "retail": """Focus on consumer sentiment, seasonal trends, competitor actions,
            economic indicators (unemployment, inflation), supply chain issues, 
            promotional activities, and foot traffic patterns.""",
            
            "energy": """Focus on oil/gas prices, renewable energy adoption, policy changes,
            weather patterns, geopolitical tensions, production cuts/increases, 
            and infrastructure developments.""",
            
            "agriculture": """Focus on weather conditions, crop yields, pest/disease outbreaks,
            trade agreements, commodity prices, planting/harvest seasons, 
            and government subsidies.""",
            
            "technology": """Focus on product launches, regulatory changes, chip shortages,
            innovation announcements, competitive dynamics, and market adoption rates."""
        }
        return contexts.get(self.domain, "Focus on general economic and market factors.")
    
    def _build_agent(self):
        """Build the LLM agent with domain-specific prompt and parser."""
        domain_context = self._get_domain_context()
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", f"""You are an expert analyst in the {self.domain} sector.
            Analyze the provided news and extract structured features for forecasting.
            {domain_context}
            
            {self.parser.get_format_instructions()}"""),
            ("user", """Date: {date}
            News Summary:
            {news_text}
            
            Extract relevant features that could impact future trends.""")
        ])
        
        return prompt | self.llm | self.parser
    
    def extract_news_features(self, news_text: str, date: str) -> Dict[str, float]:
        """
        Extract features from news text using LLM.
        
        Args:
            news_text: News articles or text for a specific date
            date: Date of the news
            
        Returns:
            Dictionary of extracted features
        """
        domain_context = self._get_domain_context()
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", f"""You are an expert analyst in the {self.domain} sector.
            Analyze the provided news and extract structured features for forecasting.
            {domain_context}
            
            {self.parser.get_format_instructions()}"""),
            ("user", """Date: {date}
            News Summary:
            {news_text}
            
            Extract relevant features that could impact future trends.""")
        ])
        
        try:
            chain = prompt | self.llm | self.parser
            result = chain.invoke({"date": date, "news_text": news_text})
            
            return {
                "news_sentiment": result.sentiment_score,
                "supply_chain_risk": result.supply_chain_risk,
                "demand_indicator": result.demand_indicator,
                "price_pressure": result.price_pressure,
                "market_volatility": result.market_volatility,
                "event_count": len(result.key_events)
            }
        except Exception as e:
            logger.error(f"Error extracting news features: {e}")
            return {
                "news_sentiment": 0.0,
                "supply_chain_risk": 0.0,
                "demand_indicator": 0.5,
                "price_pressure": 0.0,
                "market_volatility": 0.5,
                "event_count": 0
            }
    
    def add_news_features(self, df: pd.DataFrame, date_col: str, 
                         news_col: str) -> pd.DataFrame:
        """
        Add LLM-extracted news features to dataframe.
        
        Args:
            df: Input dataframe
            date_col: Name of the datetime column
            news_col: Name of the column containing news text
            
        Returns:
            DataFrame with news features added
        """
        df = df.copy()
        
        logger.info(f"Extracting news features for {self.domain} domain...")
        
        news_features_list = []
        for idx, row in df.iterrows():
            news_text = row.get(news_col, "")
            date = str(row[date_col])
            
            if pd.isna(news_text) or news_text == "":
                features = {
                    "news_sentiment": 0.0,
                    "supply_chain_risk": 0.0,
                    "demand_indicator": 0.5,
                    "price_pressure": 0.0,
                    "market_volatility": 0.5,
                    "event_count": 0
                }
            else:
                features = self.extract_news_features(news_text, date)
            
            news_features_list.append(features)
        
        news_df = pd.DataFrame(news_features_list)
        df = pd.concat([df, news_df], axis=1)
        
        return df
