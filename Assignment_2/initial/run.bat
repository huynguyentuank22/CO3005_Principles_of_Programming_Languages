@echo off
if not exist run.py (
    cd .\initial\src\
)
python run.py gen
python run.py test LexerSuite
python run.py test ParserSuite
python run.py test ASTGenSuite