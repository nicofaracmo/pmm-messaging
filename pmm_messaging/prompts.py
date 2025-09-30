SYSTEM = """
You are a Product Marketing assistant that returns STRICT JSON for downstream systems.
You help synthesize inputs into Personas → JTBD → Positioning → Messaging.
ALWAYS be concise, benefit-led, and grounded in supplied evidence.
Brand tone preset: {tone}.
"""

SEGMENT_PROMPT = """
Classify this customer snippet into one persona label from {personas} and 1-3 pains from {pains}.
Snippet: ```{snippet}```
Return JSON: {{"persona":"...", "pains":["..."]}}
"""

SYNTH_PROMPT = """
Given EVIDENCE for persona={persona}:
```
{evidence}
```
Synthesize:
1) top 3 user insights
2) a crisp VALUE PROPOSITION
3) 3 PROOF POINTS grounded in evidence
Return JSON:
{{"insights": ["...","...","..."], "value_prop": "...", "proof_points": ["...","...","..."]}}
"""

JTBD_PROMPT = """
Create a JTBD record for persona={persona} using situation/motivation/outcome.
Include barriers, essential outcomes, and irrelevant outcomes.
Return JSON:
{{"situation":"...", "motivation":"...", "expected_outcome":"...", "barriers":["..."],
"essential_outcomes":["..."], "irrelevant_outcomes":["..."]}}
"""

POSITIONING_PROMPT = """
Fill an April Dunford-style positioning statement:
For [target buyers], [offering] is a [category] that [main benefits], unlike [primary competitor] which [competitor benefit].
Using:
- Offering: {offering}
- Category: {category}
- Target buyers: {persona}
- Differentiators/Evidence: {proof_points}
Return JSON: {{"template":"For [target buyers]...", "filled":"..."}}
"""

MESSAGING_PROMPT = """
Using VALUE PROP="{value_prop}" and PROOF POINTS={proof_points}:
Generate messaging for persona={persona} in TONE={tone}:
- tagline (<=8 words)
- homepage hero (headline + 1-sentence subhead)
- 1 lifecycle email (subject + 3-sentence body)
- 1 social post (<=200 chars)
- 1 in-product nudge (<=120 chars)
Return JSON with keys: {{"tagline":"...", "hero":{{"headline":"...","subhead":"..."}}, "email":{{"subject":"...","body":"..."}}, "social":"...", "in_product":"..."}}.
"""
