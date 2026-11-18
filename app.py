import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="Semantic ML Demo", page_icon="🧠", layout="centered")

BASE = Path(__file__).resolve().parent
MODEL_CANDIDATES = [
    BASE / "artifacts" / "semantic_ml_model.joblib",
    BASE / "05_semantic_ml_model.joblib",
]

@st.cache_resource
def load_model():
    for path in MODEL_CANDIDATES:
        if path.exists():
            return joblib.load(path), path
    return None, None

st.title("Semantic ML Demo")
st.subheader("Adding a Semantic Layer (Ontology) to Machine Learning")
st.write(
    "This educational demo shows how a domain-derived semantic feature can be "
    "used together with raw measurements by a Machine Learning model."
)

with st.expander("How the semantic layer fits into the workflow", expanded=True):
    st.markdown("**Data → Ontology/RDF → Domain Knowledge → Semantic Features → ML → Prediction**")
    st.caption(
        "The ontology defines domain meaning. In the tested example, a simple rule "
        "materializes the AtRiskStudent classification, and SPARQL is used in the "
        "training pipeline to extract semantic features."
    )

col1, col2 = st.columns(2)
with col1:
    hours = st.number_input("Study hours", min_value=0, max_value=24, value=6, step=1)
with col2:
    attendance = st.number_input("Attendance %", min_value=0, max_value=100, value=75, step=1)

# Same tested demonstration rule used by the semantic enrichment pipeline.
at_risk = int(hours <= 5 and attendance <= 60)

st.markdown("### Semantic layer")
st.code("Study Hours <= 5 AND Attendance <= 60  =>  AtRiskStudent", language=None)
if at_risk:
    st.warning("Inferred/domain-derived knowledge: AtRiskStudent = True")
else:
    st.success("Inferred/domain-derived knowledge: AtRiskStudent = False")

features = pd.DataFrame([{
    "study_hours": hours,
    "attendance_pct": attendance,
    "at_risk": at_risk,
}])

st.markdown("### ML-ready features")
st.dataframe(features, hide_index=True, use_container_width=True)

model, model_path = load_model()
if model is None:
    st.error(
        "Model file not found. Run `python run_pipeline.py` locally first, or commit "
        "the generated model to `artifacts/semantic_ml_model.joblib` for Streamlit deployment."
    )
else:
    if st.button("Predict", type="primary"):
        prediction = model.predict(features)[0]
        st.markdown("### Prediction")
        st.success(str(prediction).upper())
        st.caption(f"Loaded model: {model_path.name}")

st.divider()
st.caption(
    "Educational demonstration using synthetic student data. This project demonstrates "
    "an integration pattern and does not claim that semantic enrichment automatically "
    "improves model accuracy."
)
