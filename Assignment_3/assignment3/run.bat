@echo off
if not exist run.py (
    cd .\initial\src\
)
@REM python run.py gen
@REM python run.py test CheckerSuite
python run.py test CheckSuite