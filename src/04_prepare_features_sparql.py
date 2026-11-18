from rdflib import Graph
import pandas as pd

# Load enriched semantic knowledge graph
g = Graph()

g.parse(
    "03_enriched_knowledge_graph.ttl",
    format="turtle"
)

# Query features from the semantic layer
query = """
PREFIX ex: <http://example.org/edu#>

SELECT
    ?student
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
"""

results = g.query(query)

rows = []

for row in results:

    at_risk = 1 if row.riskType is not None else 0

    rows.append({
        "student": str(row.student).split("#")[-1],
        "study_hours": int(row.hours),
        "attendance_pct": int(row.attendance),
        "at_risk": at_risk,
        "result": str(row.performance)
    })

df = pd.DataFrame(rows)

df.to_csv(
    "04_ml_features.csv",
    index=False
)

print(
    "Step 4 complete: "
    "SPARQL features -> 04_ml_features.csv"
)

print()

print(df.to_string(index=False))