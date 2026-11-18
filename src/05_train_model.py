import pandas as pd, joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

df=pd.read_csv("04_ml_features.csv")
X=df[["study_hours","attendance_pct","at_risk"]]; y=df["result"]
# Tiny educational dataset: metric below is illustrative, not evidence semantic enrichment improves accuracy.
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=0.25,random_state=42,stratify=y)
model=DecisionTreeClassifier(max_depth=3,random_state=42).fit(Xtr,ytr)
pred=model.predict(Xte)
print("Step 5 test accuracy (illustrative only):",accuracy_score(yte,pred))
print(classification_report(yte,pred,zero_division=0))
# Save a final model trained on all demo rows for the interactive app.
model.fit(X,y); joblib.dump(model,"05_semantic_ml_model.joblib")
print("Saved 05_semantic_ml_model.joblib")
