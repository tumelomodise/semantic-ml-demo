<div align="center">

# Semantic ML Demo

### Adding a Semantic Layer (Ontology) to Machine Learning

<p>
  A small, tested, end-to-end educational project demonstrating how
  <strong>OWL/RDF, semantic enrichment, SPARQL, scikit-learn, and Streamlit</strong>
  can work together in one Machine Learning pipeline.
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/RDFLib-Knowledge_Graph-2E8B57?style=for-the-badge" alt="RDFLib">
  <img src="https://img.shields.io/badge/SPARQL-Feature_Extraction-6A5ACD?style=for-the-badge" alt="SPARQL">
  <img src="https://img.shields.io/badge/scikit--learn-Decision_Tree-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="scikit-learn">
</p>

<p>
  <strong>Data + Meaning + Machine Learning = More Context-Aware AI</strong>
</p>

<!-- Replace the two placeholder links below after deployment. -->
<p>
  <a href="YOUR_STREAMLIT_APP_URL"><strong>Try the live app</strong></a>
  &nbsp;•&nbsp;
  <a href="YOUR_GITHUB_REPOSITORY_URL"><strong>View the source code</strong></a>
</p>

</div>

---

## Overview

A conventional Machine Learning workflow often looks like this:

<div align="center">
  <strong>Data → Features → ML Model → Prediction</strong>
</div>

This project adds a semantic layer:

<div align="center">
  <strong>Data → Ontology → RDF Knowledge Graph → Semantic Enrichment → SPARQL Features → ML Model → Prediction</strong>
</div>

The ontology provides a domain vocabulary. RDF represents the data as a knowledge graph. A domain rule adds an explicit classification, SPARQL extracts the original and derived knowledge as ML-ready features, and a Decision Tree uses those features to make a prediction.

> This is a deliberately small educational demonstration. It illustrates an integration pattern and does not claim that adding semantic features automatically improves model accuracy.

---

## The Example

The synthetic dataset contains student study hours, attendance percentages, and outcomes.

A simple domain rule is applied:

<div align="center">

| Condition | Logical operator | Condition | Derived knowledge |
|---|:---:|---|---|
| `Study Hours <= 5` | **AND** | `Attendance <= 60` | `AtRiskStudent` |

</div>

The derived `AtRiskStudent` classification becomes an `at_risk` feature that the ML model can consume together with the original measurements.

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
    <td><strong>1. Define the ontology</strong></td>
    <td>Define domain concepts and properties.</td>
    <td>Protégé or OWL/RDF/XML</td>
    <td><code>education_ontology.owl</code></td>
  </tr>
  <tr>
    <td><strong>2. Map data to RDF</strong></td>
    <td>Transform CSV rows into RDF triples.</td>
    <td>Python + RDFLib</td>
    <td><code>knowledge_graph.ttl</code></td>
  </tr>
  <tr>
    <td><strong>3. Enrich with domain knowledge</strong></td>
    <td>Add the derived <code>AtRiskStudent</code> classification.</td>
    <td>Rule-based semantic enrichment</td>
    <td><code>enriched_knowledge_graph.ttl</code></td>
  </tr>
  <tr>
    <td><strong>4. Prepare semantic features</strong></td>
    <td>Query original and derived knowledge.</td>
    <td>SPARQL</td>
    <td><code>ml_features.csv</code></td>
  </tr>
  <tr>
    <td><strong>5. Train the ML model</strong></td>
    <td>Train a classifier with raw and domain-derived features.</td>
    <td>scikit-learn</td>
    <td><code>semantic_ml_model.joblib</code></td>
  </tr>
  <tr>
    <td><strong>6. Test the solution</strong></td>
    <td>Enter values and inspect the semantic feature and prediction.</td>
    <td>Streamlit</td>
    <td>Interactive web application</td>
  </tr>
</table>

---

## Ontology Creation Options

### Option 1: Protégé

[Protégé](https://protege.stanford.edu/) can be used to create and inspect the ontology visually. The ontology includes:

- Classes: `Student` and `AtRiskStudent`
- Datatype properties: `hasStudyHours`, `hasAttendance`, and `hasPerformance`
- Class relationship: `AtRiskStudent` is a subclass of `Student`

### Option 2: OWL/RDF/XML

For this small example, the ontology can also be written directly as an `.owl` file using RDF/XML. This makes the project testable without requiring users to learn the Protégé interface first.

> `StudyHours`, `Attendance`, and `Performance` are represented as datatype properties because their values are literals, not ontology classes.

---

## Project Structure

```text
semantic-ml-demo/
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

If the repository still uses numbered files in the root directory, update this tree to match the final structure before publishing.

---

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd semantic-ml-demo
```

### 2. Create a virtual environment

#### Windows Command Prompt

```cmd
python -m venv .venv
.venv\Scripts\activate
```

#### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

#### Linux or macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Run the Complete Pipeline

```bash
python run_pipeline.py
```

The pipeline should:

1. Map the CSV data into an RDF knowledge graph.
2. Add the `AtRiskStudent` classifications.
3. execute the SPARQL feature query.
4. Create the ML-ready feature dataset.
5. Train and save the Decision Tree model.

Expected generated artifacts:

```text
knowledge_graph.ttl
enriched_knowledge_graph.ttl
ml_features.csv
semantic_ml_model.joblib
```

---

## Run the Streamlit Application

After the pipeline completes successfully, run:

```bash
python -m streamlit run app.py
```

The browser should open at:

```text
http://localhost:8501
```

Try these example inputs:

<table>
  <tr>
    <th>Study hours</th>
    <th>Attendance</th>
    <th>Expected semantic feature</th>
  </tr>
  <tr>
    <td>2</td>
    <td>50</td>
    <td><code>at_risk = 1</code></td>
  </tr>
  <tr>
    <td>8</td>
    <td>80</td>
    <td><code>at_risk = 0</code></td>
  </tr>
</table>

---

## SPARQL Feature Extraction

The project queries the enriched graph with SPARQL. The `OPTIONAL` pattern checks whether each student has been classified as an `AtRiskStudent`.

```sparql
PREFIX ex: <http://example.org/edu#>

SELECT ?student ?hours ?attendance ?performance ?riskType
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

The query results are converted into a feature table similar to:

| study_hours | attendance_pct | at_risk | result |
|---:|---:|---:|---|
| 2 | 50 | 1 | fail |
| 4 | 60 | 1 | fail |
| 6 | 70 | 0 | pass |
| 8 | 80 | 0 | pass |

---

## Deploy on Streamlit Community Cloud

1. Push the project to a public GitHub repository.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Select **Create app**.
4. Choose the repository and branch.
5. Set the main file path to `app.py`.
6. Deploy the application.
7. Replace `YOUR_STREAMLIT_APP_URL` at the top of this README with the generated URL.

The deployed application must not depend on a user manually running `run_pipeline.py`. Use one of these approaches:

- Commit the small generated model and semantic artifacts to the repository, or
- Make `app.py` build missing artifacts automatically and cache the result with `st.cache_resource` or `st.cache_data`.

---

## Technology Stack

<div align="center">

| Layer | Technology |
|---|---|
| Ontology authoring | Protégé or OWL/RDF/XML |
| Semantic representation | RDF |
| Knowledge graph processing | RDFLib |
| Semantic feature query | SPARQL |
| Data processing | pandas |
| Machine Learning | scikit-learn |
| Model persistence | joblib |
| User interface | Streamlit |

</div>

---

## Important Technical Notes

- The ontology defines the semantic vocabulary.
- The RDF graph stores the instance data and relationships.
- The numeric domain rule is materialized explicitly in Python.
- A plain OWL reasoner call is not presented as automatically implementing the numeric rule.
- SPARQL extracts features from the enriched semantic graph.
- The small synthetic dataset is suitable for demonstrating the architecture, not for proving production accuracy or performance improvements.
- The `at_risk` feature is derived from existing inputs, so its predictive value must be evaluated on a larger and properly designed dataset before drawing conclusions.

---

## Public-Use and Data Disclaimer

This repository is a self-contained educational project using synthetic student data.

The repository does not contain confidential organisational information, production architecture, taxpayer information, credentials, personal data, internal system identifiers, or proprietary source code.

The project is not presented as a production solution or as evidence that a semantic layer automatically improves model accuracy.

---

## Contributing

Suggestions and educational improvements are welcome. Possible extensions include:

- Creating and editing the ontology in Protégé
- Adding SHACL validation
- Introducing a dedicated rule engine
- Comparing the model with and without semantic features
- Adding cross-validation and a larger synthetic dataset
- Displaying RDF triples and SPARQL results inside the Streamlit app
- Adding model explainability with feature importance or SHAP

---

## License

Add a license before publishing the repository. The [MIT License](https://opensource.org/license/mit) is a common choice for a small educational code project.

---

<div align="center">

### Use knowledge, not just data, to build smarter models.

**Semantic technologies complement Machine Learning rather than replace it.**

</div>
