import subprocess,sys
steps=["02_map_data_to_ontology.py","03_enrich_with_reasoning.py","04_prepare_features_sparql.py","05_train_model.py"]
for step in steps:
    print("\n===",step,"===")
    subprocess.run([sys.executable,step],check=True)
print("\nPipeline complete. Run: streamlit run 06_semantic_ml_app.py")
