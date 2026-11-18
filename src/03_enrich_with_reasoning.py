from rdflib import Graph, Namespace
from rdflib.namespace import RDF
EX=Namespace("http://example.org/edu#")
g=Graph(); g.parse("artifacts/knowledge_graph.ttl",format="turtle")
# Demonstration semantic/domain rule intentionally materialized in Python:
# StudyHours <= 5 AND Attendance <= 60 => AtRiskStudent.
# This is rule-based semantic enrichment, not a claim that OWL DL alone executes this numeric rule.
added=0
for student in set(g.subjects(RDF.type,EX.Student)):
    hours=next(g.objects(student,EX.hasStudyHours),None)
    attendance=next(g.objects(student,EX.hasAttendance),None)
    if hours is not None and attendance is not None and int(hours)<=5 and int(attendance)<=60:
        triple=(student,RDF.type,EX.AtRiskStudent)
        if triple not in g:
            g.add(triple); added+=1
g.serialize("03_enriched_knowledge_graph.ttl",format="turtle")
print(f"Step 3 complete: added {added} AtRiskStudent classifications -> artifacts/enriched_knowledge_graph.ttl")
