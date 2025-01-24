# MLops_practice_project
This project is one of the practice project to implement all the things we learn until learn.
Also save it for future reference Complete AI software Deployment with CI/CD.
Thank You!

STEPS:
1. create requirements.txt (pip install -r requirements.txt)
2. create setup.py
3. before run setup.py '''create src package(by adding __init__.py) in a src folder for check'''
4. run setup.py
###### components: components are the steps we follows in training pipeline(data source,data ingestion, data transformation,model trainer,model monitoring,CI/CD pipeline,model deployment)
5. create template.py  (responsible for creating the entire project structure)
6. code in template.py  # we have to things in our project [components & pipeline(training, testing)]
7. run template.py  (python template.py)
8. we can also use cookiecutter(optional)
9. Write code on logger.py
10. Write code for exception.py
11. create .env variable (store database connection )
12. write code in utils.py (for database connection)
13. Start data ingestion(open components/data_ingestion.py)
14. write code for run data ingestion in app.py
15. use DVC(data version control) for track data like git (for big data)
16.  DVC Commands
#### dvc init, dvc add artifacts/raw.csv,
17. use jupyter for research for training(USE EDA,model_training)
# now do the notebook code in pipeline format
18. write code in data_transformation.py(feature_engineering)
19. 