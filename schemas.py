from pydantic import BaseModel
from typing import List, Optional

class ActionItem(BaseModel):
    action: str
    owner: Optional[str]
    deadline: Optional[str]

class Risk(BaseModel):
    category: str  # Operational, Legal, Financial, Strategic
    description: str

class DocumentInsights(BaseModel):
    risks: List[Risk]
    action_items: List[ActionItem]

