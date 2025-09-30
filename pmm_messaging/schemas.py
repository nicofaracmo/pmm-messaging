from pydantic import BaseModel, Field
from typing import List, Literal, Optional, Dict

class Persona(BaseModel):
    name: str
    segment_type: Literal["B2C","B2B"]
    role_in_buying_process: Optional[str] = None
    bio: Optional[str] = None
    background: Dict[str, Optional[str]] = {}
    demographics: Dict[str, Optional[str]] = {}
    personal_details: Dict[str, Optional[str]] = {}
    responsibilities: List[str] = []
    motivators: List[str] = []
    goals: List[str] = []
    challenges: List[str] = []
    emotional_drivers: List[str] = []
    real_quotes: List[str] = []
    comm_prefs: List[str] = []
    confidence: float = Field(ge=0, le=1, default=0.5)

class JTBD(BaseModel):
    situation: str
    motivation: str
    expected_outcome: str
    barriers: List[str] = []
    essential_outcomes: List[str] = []
    irrelevant_outcomes: List[str] = []

class Positioning(BaseModel):
    template: str
    filled: str

class Messaging(BaseModel):
    tagline: str
    hero: Dict[str, str]
    email: Dict[str, str]
    social: str
    in_product: str
