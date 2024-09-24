@echo off
echo Instalando dependências do Python...
cd IA
pip install mediapipe requests opencv-python

if errorlevel 1 (
    cls
    echo Algo deu errado ao instalar as dependências do Python. Verifique se o pip está instalado e se você tem acesso à internet.
    pause
    exit /b
)

cls
echo Instalando OpenCV...
pip install opencv-python

if errorlevel 1 (
    cls
    echo Algo deu errado ao instalar OpenCV. Tente instalar manualmente ou veja se tem acesso à internet.
) else (
    cls
    echo Todas as dependências do Python instaladas com sucesso!
)

pause
