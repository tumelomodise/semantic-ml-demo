<div align="center">

# Semantic ML Demo

### Adding a Semantic Layer (Ontology) to Machine Learning

<p>
  A tested, end-to-end educational project demonstrating how
  <strong>OWL/RDF, semantic enrichment, SPARQL, scikit-learn, and Streamlit</strong>
  can work together in a Machine Learning pipeline.
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit Live App">
  <img src="https://img.shields.io/badge/RDFLib-Knowledge_Graph-2E8B57?style=for-the-badge" alt="RDFLib">
  <img src="https://img.shields.io/badge/SPARQL-Feature_Extraction-6A5ACD?style=for-the-badge" alt="SPARQL">
  <img src="https://img.shields.io/badge/scikit--learn-Decision_Tree-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="scikit-learn">
</p>

<p>
  <a href="https://semantic-ml-demo-26ltmdt4sng65mtafumjrq.streamlit.app/">
    <strong>🚀 Try the Live App</strong>
  </a>
  &nbsp;•&nbsp;
  <a href="https://github.com/tumelomodise/semantic-ml-demo">
    <strong>💻 View the Source Code</strong>
  </a>
</p>

<p>
  <strong>Data + Meaning + Machine Learning = More Context-Aware AI</strong>
</p>

</div>

---

<p align="center">
  <img
    src="assets/semantic-ml-poster.png"
    alt="Semantic Machine Learning workflow showing ontology, RDF, semantic enrichment, SPARQL, Machine Learning, and Streamlit"
    width="900"
  />
</p>

---

## Overview

A conventional Machine Learning workflow often looks like this:

<div align="center">

**Data → Features → ML Model → Prediction**

</div>

This project adds a semantic layer:

<div align="center">

**Data → Ontology → RDF Knowledge Graph → Semantic Enrichment → SPARQL Features → ML Model → Prediction**

</div>

The ontology defines the **domain vocabulary**.

RDF represents the data as a **knowledge graph**.

A domain rule enriches the graph with an additional classification.

SPARQL extracts the original and domain-derived knowledge as **ML-ready features**, and a Decision Tree consumes those features to produce a prediction.

> This is a deliberately small educational demonstration. It illustrates an integration pattern and does not claim that semantic enrichment automatically improves model accuracy.

---

## 🚀 Try the Live Demo

The project is deployed on Streamlit Community Cloud:

**Live Application:**  
https://semantic-ml-demo-26ltmdt4sng65mtafumjrq.streamlit.app/

Try these example inputs:

| Study Hours | Attendance | Semantic Result | ML Feature |
|---:|---:|---|---:|
| 2 | 50 | `AtRiskStudent = True` | `at_risk = 1` |
| 4 | 60 | `AtRiskStudent = True` | `at_risk = 1` |
| 8 | 80 | `AtRiskStudent = False` | `at_risk = 0` |

The demonstration domain rule is:

```text
Study Hours <= 5
        +
Attendance <= 60
        ↓
AtRiskStudent
```

The derived knowledge can then become another feature available to the Machine Learning model.

---

## Semantic ML Workflow

<table>
  <tr>
    <th>Step</th>
    <th>Purpose</th>
    <th>Technology</th>
    <th>Output</th>
  </tr>

  <tr>
    <td><strong>1. Define the Ontology</strong></td>
    <td>Define domain concepts and datatype properties.</td>
    <td>Protégé or OWL/RDF/XML</td>
    <td><code>education_ontology.owl</code></td>
  </tr>

  <tr>
    <td><strong>2. Map Data to RDF</strong></td>
    <td>Transform synthetic CSV rows into RDF triples.</td>
    <td>Python + RDFLib</td>
    <td><code>knowledge_graph.ttl</code></td>
  </tr>

  <tr>
    <td><strong>3. Enrich with Domain Knowledge</strong></td>
    <td>Add the derived <code>AtRiskStudent</code> classification.</td>
    <td>Rule-based semantic enrichment</td>
    <td><code>enriched_knowledge_graph.ttl</code></td>
  </tr>

  <tr>
    <td><strong>4. Prepare Semantic Features</strong></td>
    <td>Query original and domain-derived knowledge.</td>
    <td>SPARQL</td>
    <td><code>ml_features.csv</code></td>
  </tr>

  <tr>
    <td><strong>5. Train the ML Model</strong></td>
    <td>Train a classifier using raw and domain-derived features.</td>
    <td>scikit-learn</td>
    <td><code>semantic_ml_model.joblib</code></td>
  </tr>

  <tr>
    <td><strong>6. Test the Solution</strong></td>
    <td>Inspect the semantic feature and request a prediction.</td>
    <td>Streamlit</td>
    <td>Interactive web application</td>
  </tr>
</table>

---

## 1. Define the Ontology

The first step is to define the vocabulary used by the semantic layer.

The demonstration ontology contains concepts such as:

```text
Student
AtRiskStudent
```

and datatype properties such as:

```text
hasStudyHours
hasAttendance
hasPerformance
```

### Option 1: Protégé

[Protégé](https://protege.stanford.edu/) can be used to visually create, edit, and inspect the ontology.

For example:

```text
Student
   ↑
   │ subclass
   │
AtRiskStudent
```

### Option 2: OWL/RDF/XML

For this small demonstration, the ontology can also be defined directly in an `.owl` file using RDF/XML.

This makes it possible to test the project without first learning the Protégé interface.

> `StudyHours`, `Attendance`, and `Performance` are represented using datatype properties because their values are literals rather than ontology classes.

---

## 2. Map the Data to RDF

The synthetic student dataset is transformed from tabular data into RDF triples using Python and RDFLib.

Conceptually:

```text
student_performance.csv
        ↓
     RDFLib
        ↓
knowledge_graph.ttl
```

A student can then be represented semantically as:

```text
Student
 ├── hasStudyHours
 ├── hasAttendance
 └── hasPerformance
```

---

## 3. Enrich with Domain Knowledge

The next step adds domain-derived knowledge to the RDF graph.

The demonstration rule is:

```text
Study Hours <= 5
AND
Attendance <= 60
        ↓
AtRiskStudent
```

When the condition is true, the graph is enriched with an additional RDF classification:

```text
Student
   rdf:type
       ↓
AtRiskStudent
```

This is **rule-based semantic enrichment** implemented explicitly in Python.

The example does not assume that a plain OWL reasoner automatically implements this numeric business rule.

---

## 4. Prepare Features with SPARQL

After enrichment, SPARQL queries the semantic layer and extracts both original and domain-derived knowledge.

```sparql
PREFIX ex: <http://example.org/edu#>

SELECT ?student
       ?hours
       ?attendance
       ?performance
       ?riskType
WHERE {

  ?student a ex:Student ;
           ex:hasStudyHours ?hours ;
           ex:hasAttendance ?attendance ;
           ex:hasPerformance ?performance .

  OPTIONAL {
    ?student a ex:AtRiskStudent .
    BIND("AtRisk" AS ?riskType)
  }
}

ORDER BY ?student
```

The SPARQL results are converted into an ML-ready feature table:

| study_hours | attendance_pct | at_risk | result |
|---:|---:|---:|---|
| 2 | 50 | 1 | fail |
| 4 | 60 | 1 | fail |
| 6 | 70 | 0 | pass |
| 8 | 80 | 0 | pass |

This provides the Machine Learning model with:

```text
study_hours
attendance_pct
at_risk
```

---

## 5. Train the Machine Learning Model

The project uses a `DecisionTreeClassifier` from scikit-learn.

```python
from sklearn.tree import DecisionTreeClassifier

X = df[
    [
        "study_hours",
        "attendance_pct",
        "at_risk"
    ]
]

y = df["result"]

model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

model.fit(X, y)
```

The important distinction is:

> **The semantic layer describes what the data means.**

> **Machine Learning learns patterns from the resulting features.**

The ontology does not replace Machine Learning. The technologies complement one another.

---

## 6. Test with Streamlit

The Streamlit application provides an interactive interface for the demonstration.

Users can enter:

```text
Study Hours
Attendance %
```

The application derives:

```text
AtRiskStudent
```

and creates the ML feature:

```text
at_risk
```

before sending the feature set to the trained model.

### Live App

https://semantic-ml-demo-26ltmdt4sng65mtafumjrq.streamlit.app/

---

## Repository Structure

```text
semantic-ml-demo/
│
├── README.md
├── requirements.txt
├── .gitignore
├── app.py
├── run_pipeline.py
│
├── data/
│   └── student_performance.csv
│
├── ontology/
│   └── education_ontology.owl
│
├── src/
│   ├── map_data_to_ontology.py
│   ├── enrich_with_reasoning.py
│   ├── prepare_features_sparql.py
│   └── train_model.py
│
├── artifacts/
│   ├── knowledge_graph.ttl
│   ├── enriched_knowledge_graph.ttl
│   ├── ml_features.csv
│   └── semantic_ml_model.joblib
│
└── assets/
    └── semantic-ml-poster.png
```

---

## Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/tumelomodise/semantic-ml-demo.git
cd semantic-ml-demo
```

### 2. Create a virtual environment

#### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
python -m venv .venv
.venv\Scripts\activate
```

#### Linux or macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the semantic ML pipeline

```bash
python run_pipeline.py
```

The pipeline:

```text
CSV Data
    ↓
RDF Knowledge Graph
    ↓
Semantic Enrichment
    ↓
SPARQL
    ↓
ML Features
    ↓
Decision Tree
```

### 5. Start Streamlit

```bash
python -m streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

## Technology Stack

| Layer | Technology |
|---|---|
| Ontology authoring | Protégé / OWL/RDF/XML |
| Semantic representation | RDF |
| Knowledge graph processing | RDFLib |
| Semantic querying | SPARQL |
| Data processing | pandas |
| Machine Learning | scikit-learn |
| Model | Decision Tree |
| Model persistence | joblib |
| User interface | Streamlit |
| Source control | GitHub |
| Deployment | Streamlit Community Cloud |

---

## Technical Notes

- The ontology defines the domain vocabulary.
- RDF represents the instance data and semantic relationships.
- The numeric domain rule is materialized explicitly in Python.
- SPARQL extracts features from the enriched RDF graph.
- `at_risk` is a domain-derived feature based on `study_hours` and `attendance_pct`.
- The dataset is deliberately small and synthetic.
- The project demonstrates architecture and integration, not production-scale predictive performance.
- The project does **not** claim that adding a semantic layer automatically improves model accuracy.
- A proper performance study would require a larger dataset, a baseline model, cross-validation, leakage analysis, and suitable evaluation metrics.

---

## Educational and Public-Use Disclaimer

This repository is a **self-contained educational project using synthetic student data**.

The project does not contain confidential organisational information, taxpayer information, production architecture, credentials, personal information, internal system identifiers, or proprietary source code.

The project is not presented as a production architecture or as evidence that semantic enrichment automatically improves Machine Learning accuracy.

---

## Possible Extensions

Some ideas for extending the project:

- Create and modify the ontology using **Protégé**
- Add **SHACL** data validation
- Introduce a dedicated semantic rule engine
- Compare models **with and without** semantic features
- Use a larger synthetic dataset
- Add cross-validation
- Display RDF triples directly in Streamlit
- Display SPARQL results interactively
- Visualize the knowledge graph
- Add Decision Tree feature importance
- Add SHAP-based model explanations
- Add automated tests
- Add a GitHub Actions CI workflow

---

## Live Project

🚀 **Try the Streamlit application**

https://-demo-26ltmdt4sng65mtafumjrq.streamlit.app/

💻 **Explore the source code**

https://github.com/tumelomodise/semantic-ml-demo

---

<div align="center">

### Use knowledge, not just data, to build smarter models.

**Semantic technologies complement Machine Learning rather than replace it.**

<br>

<a href="https://semantic-ml-demo-26ltmdt4sng65mtafumjrq.streamlit.app/">
  <strong>🚀 Launch the App</strong>
</a>

&nbsp; • &nbsp;

<a href="https://github.com/tumelomodise/semantic-ml-demo">
  <strong>💻 Explore the Repository</strong>
</a>

</div>
