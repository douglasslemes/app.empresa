import json
from app.models import Funcionario

DATA_FILE = "data/funcionarios.json"

def carregar_dados():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Funcionario.from_dict(funcionario) for funcionario in data]
    except FileNotFoundError:
        return []

def salvar_dados(funcionarios):
    data = [funcionario.to_dict() for funcionario in funcionarios]
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)