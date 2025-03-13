@echo off
if not exist run.py (
    cd .\initial\src\
)
python run.py gen
python run.py test CheckerSuite
python run.py test CheckSuite