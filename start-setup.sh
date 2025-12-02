#!/bin/bash

echo "Creating virtual environment... / Criando ambiente virtual..."
python3 -m venv venv

echo "Activating virtual environment... / Ativando ambiente virtual..."
source venv/bin/activate

echo "Upgrading pip... / Atualizando pip..."
pip install --upgrade pip

echo "Installing dependencies... / Instalando dependências..."
pip install -r requirements.txt

echo "Environment setup complete. To activate it next time, run: / Configuração do ambiente concluída. Para ativar na próxima vez, execute:"
echo "source venv/bin/activate"
