from typing import List, Dict, Any
from . import prompts
from .llm import chat_json

DEFAULT_PERSONAS = ["Buyer-Mobile","Buyer-Trust","Buyer-Power","Seller-SMB","Seller-Pro"]
DEFAULT_PAINS = ["Speed","Clarity/Trust","Tooling/Workflow","Fees/Pricing","Relevance"]

def segment_snippet(snippet: str, tone: str, personas=DEFAULT_PERSONAS, pains=DEFAULT_PAINS) -> Dict[str, Any]:
    system = prompts.SYSTEM.format(tone=tone)
    user = prompts.SEGMENT_PROMPT.format(snippet=snippet, personas=personas, pains=pains)
    return chat_json(system, user)

def synthesize_for_persona(persona: str, evidence: str, tone: str) -> Dict[str, Any]:
    system = prompts.SYSTEM.format(tone=tone)
    user = prompts.SYNTH_PROMPT.format(persona=persona, evidence=evidence)
    return chat_json(system, user)

def make_jtbd(persona: str, tone: str) -> Dict[str, Any]:
    system = prompts.SYSTEM.format(tone=tone)
    user = prompts.JTBD_PROMPT.format(persona=persona)
    return chat_json(system, user)

def make_positioning(persona: str, offering: str, category: str, proof_points: List[str], tone: str) -> Dict[str, Any]:
    system = prompts.SYSTEM.format(tone=tone)
    user = prompts.POSITIONING_PROMPT.format(persona=persona, offering=offering, category=category, proof_points=proof_points)
    return chat_json(system, user)

def make_messaging(persona: str, value_prop: str, proof_points: List[str], tone: str) -> Dict[str, Any]:
    system = prompts.SYSTEM.format(tone=tone)
    user = prompts.MESSAGING_PROMPT.format(value_prop=value_prop, proof_points=proof_points, persona=persona, tone=tone)
    return chat_json(system, user)
