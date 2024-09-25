@echo off
echo Instalando dependências do Node.js...
cd TV
npm install

if errorlevel 1 (
    cls
    echo Algo deu errado ao instalar as dependências do Node.js. Tente instalar manualmente ou veja se tem acesso à internet.
    pause
    exit /b
)

cls
echo Dependências do Node.js instaladas com sucesso!
pause
