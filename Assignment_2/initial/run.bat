@echo off
if not exist run.py (
    cd .\initial\src\
)
python run.py gen
@REM python run.py test LexerSuite
@REM python run.py test ParserSuite
python run.py test ASTGenSuite