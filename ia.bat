@echo off
echo Iniciando o script Python...
cd IA
py index.py

if errorlevel 1 (
    echo Ocorreu um erro ao executar o script Python.
) else (
    echo Script Python executado com sucesso.
)

pause