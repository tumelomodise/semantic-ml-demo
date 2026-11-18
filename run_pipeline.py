import subprocess,sys
steps=["src/02_map_data_to_ontology.py","src/03_enrich_with_reasoning.py","src/04_prepare_features_sparql.py","src/05_train_model.py"]
for step in steps:
    print("\n===",step,"===")
    subprocess.run([sys.executable,step],check=True)
print("\nPipeline complete. Run: streamlit run 06_semantic_ml_app.py")
