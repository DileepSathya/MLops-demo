import os
from pathlib import Path    #it will takecare of the path i.e in windows for path we use '\' where as in linux we use '/' in paths this library will takecare of these things
list_of_files=[
    ".github/workflows/.gitkeep",
"src/__init__.py",
"src/components/__init__.py",
"src/components/data_ingestion.py",
"src/components/data_transformation.py",
"src/components/model_trainer.py",
"src/components/model_evaluation.py",
"src/pipeline/__init__.py",
"src/pipeline/training_pipeline.py",
"src/pipeline/prediction_pipeline.py",
"src/utils/utils.py",
"src/utils/__init__.py",
"src/logger/logging.py"
"src/exception/exception.py"
"tests/unit/__init__.py",
"tests/integration/__init__.py",            #combine all the units and test all at once
"init_setup.sh",
"requirements.txt",                          #for production
"requirements_dev.txt",                      #for development
"setup.py",
"setup.cfg",
"pyprojects.toml",
"tox.ini",
"experiments/experiments.ipynb"
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file