@echo off
echo Iniciando o servidor Node.js...
cd TV
node .

if errorlevel 1 (
    echo Ocorreu um erro ao iniciar o Node.js.
) else (
    echo Node.js iniciado com sucesso.
)



pause
