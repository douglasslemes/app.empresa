import json
from app.models import Funcionario
from app.utils import carregar_dados, salvar_dados

funcionarios = carregar_dados()

def cadastrar_funcionario(nome, cargo, salario, departamento):
    funcionario = Funcionario(nome, cargo, salario, departamento)
    funcionarios.append(funcionario)
    salvar_dados(funcionarios)

def listar_funcionarios():
    return funcionarios

def buscar_funcionario(nome):
    for funcionario in funcionarios:
        if funcionario.nome.lower() == nome.lower():
            return funcionario
    return None

def editar_funcionario(nome, novo_cargo, novo_salario, novo_departamento):
    funcionario = buscar_funcionario(nome)
    if funcionario:
        funcionario.cargo = novo_cargo
        funcionario.salario = novo_salario
        funcionario.departamento = novo_departamento
        salvar_dados(funcionarios)
        return True
    return False

def excluir_funcionario(nome):
    funcionario = buscar_funcionario(nome)
    if funcionario:
        funcionarios.remove(funcionario)
        salvar_dados(funcionarios)
        return True
    return False