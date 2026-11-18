import pandas as pd
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, XSD
EX=Namespace("http://example.org/edu#")
df=pd.read_csv("data/student_performance.csv")
g=Graph(); g.bind("ex",EX)
for _,r in df.iterrows():
    s=URIRef(EX[str(r.student_id)])
    g.add((s,RDF.type,EX.Student))
    g.add((s,EX.hasStudyHours,Literal(int(r.study_hours),datatype=XSD.integer)))
    g.add((s,EX.hasAttendance,Literal(int(r.attendance_pct),datatype=XSD.integer)))
    g.add((s,EX.hasPerformance,Literal(str(r.result))))
g.serialize("02_knowledge_graph.ttl",format="turtle")
print(f"Step 2 complete: {len(g)} triples -> knowledge_graph.ttl")
