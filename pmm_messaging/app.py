import os

import streamlit as st
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from pmm_messaging.agent import (
    segment_snippet, synthesize_for_persona, make_jtbd, make_positioning, make_messaging
)

load_dotenv()
print("API KEY visible?", bool(os.getenv("OPENAI_API_KEY")))

st.set_page_config(page_title="PMM Insights → Messaging Agent", layout="wide")
st.title("PMM Insights → Personas → JTBD → Positioning → Messaging")

with st.sidebar:
    st.header("Inputs")
    tone = st.selectbox("Tone preset", ["Retail-concise","SMB-reassuring","Pro-technical","Luxury-editorial"])
    offering = st.text_input("Offering / Product Name", value="Your Product")
    category = st.text_input("Category", value="VR Experience")
    st.markdown("#### Upload evidence CSV (columns: text, source, segment_hint)")
    file = st.file_uploader("Evidence CSV", type=["csv"])

    st.markdown("---")
    st.caption("Set OPENAI_API_KEY in your .env")

if not file:
    st.info("Upload a CSV to begin. A small sample is included in `data/sample_data.csv`.")
    st.stop()

df = pd.read_csv(file)
st.subheader("Evidence")
st.dataframe(df, use_container_width=True)

if st.button("1) Segment Snippets"):
    seg = df["text"].apply(lambda t: segment_snippet(t, tone))
    df["persona"] = seg.apply(lambda r: r.get("persona","?"))
    df["pains"] = seg.apply(lambda r: ", ".join(r.get("pains", [])) if isinstance(r.get("pains"), list) else r.get("pains", ""))
    st.success("Segmented snippets.")
    st.dataframe(df, use_container_width=True)

if "persona" not in df.columns:
    st.warning("Run segmentation first.")
    st.stop()

personas = sorted(df["persona"].dropna().unique().tolist())
st.subheader("Personas detected")
st.write(personas)

selected = st.multiselect("Select personas to synthesize", personas, default=personas[:1])

outputs = []

if st.button("2) Synthesize → JTBD → Positioning → Messaging"):
    for p in selected:
        evidence = "\n".join(df[df["persona"]==p]["text"].tolist()[:40])
        synth = synthesize_for_persona(p, evidence, tone)
        jtbd = make_jtbd(p, tone)
        pos = make_positioning(p, offering, category, synth.get("proof_points", []), tone)
        msg = make_messaging(p, synth.get("value_prop",""), synth.get("proof_points", []), tone)

        outputs.append({
            "persona": p,
            "insights": synth.get("insights", []),
            "value_prop": synth.get("value_prop", ""),
            "proof_points": synth.get("proof_points", []),
            "jtbd": jtbd,
            "positioning": pos,
            "messaging": msg
        })

    st.success("Synthesis complete.")
    for out in outputs:
        with st.expander(f"Persona: {out['persona']}"):
            st.markdown("**Value Prop**")
            st.write(out["value_prop"])
            st.markdown("**Insights**")
            st.write(out["insights"])
            st.markdown("**JTBD**")
            st.json(out["jtbd"])
            st.markdown("**Positioning**")
            st.json(out["positioning"])
            st.markdown("**Messaging**")
            st.json(out["messaging"])

    st.download_button(
        "Download JSON Outputs",
        data=pd.Series(outputs).to_json(orient="values", force_ascii=False, indent=2),
        file_name="outputs.json",
        mime="application/json"
    )

st.caption("Prototype: Streamlit + OpenAI + (optional) LangChain orchestration layers.")
