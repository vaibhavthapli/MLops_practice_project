# MLops_practice_project
This project is one of the practice project to implement all the things we learn until learn.
Also save it for future reference Complete AI software Deployment with CI/CD.
Thank You!

STEPS:
1. create requirements.txt (pip install -r requirements.txt)
2. create setup.py
3. before run setup.py '''create src package(by adding __init__.py) in a src folder for check'''
4. run setup.py(python setup.py install)
###### components: components are the steps we follows in training pipeline(data source,data ingestion, data transformation,model trainer,model monitoring,CI/CD pipeline,model deployment)
5. create template.py  (responsible for creating the entire project structure)
6. code in template.py  # we have to things in our project [components & pipeline(training, testing)]
7. run template.py  (python template.py)
8. we can also use cookiecutter(optional)
9. Write code on logger.py
10. Write code for exception.py
11. create .env variable (store database connection )
12. write code in utils.py read_sql_data(for database connection)
13. Start data ingestion(open components/data_ingestion.py)
14. write code for run data ingestion in app.py
15. use DVC(data version control) for track data like git (for big data)
16.  DVC Commands
#### dvc init, dvc add artifacts/raw.csv,
17. use jupyter for research for training(USE EDA,model_training)
# now do the notebook code in pipeline format
18. write code in data_transformation.py(feature_engineering)
19. create save_object def in utils
20. write code for model_trainer.py
21. update utils
22.  after complete components ( time to build pipeline)
23. 1- Prediction_pipeline
24. create new app.py
25. create folder templates (index.html, home.html)
26. write code in both 
27. write code in training_pipeline.py
28. write code in app.py(flask)
29. run app.py(python app.py)
30. check on crome (127.0.0.1:5000)
31. call(127.0.0.1:5000/predictdata)


![Screenshot from 2025-02-11 01-12-01](https://github.com/user-attachments/assets/9c1db604-06b4-45a2-a070-ec33961312a2)
