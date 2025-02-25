from app.controllers import (
    cadastrar_funcionario,
    listar_funcionarios,
    buscar_funcionario,
    editar_funcionario,
    excluir_funcionario,
)

def exibir_menu():
    print("1. Cadastrar funcionário")
    print("2. Listar funcionários")
    print("3. Buscar funcionário")
    print("4. Editar funcionário")
    print("5. Excluir funcionário")
    print("6. Sair")

def obter_dados_funcionario():
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    salario = float(input("Salário: "))
    departamento = input("Departamento: ")
    return nome, cargo, salario, departamento

def exibir_funcionario(funcionario):
    if funcionario:
        print(funcionario)
    else:
        print("Funcionário não encontrado.")

def obter_novos_dados_funcionario():
    novo_cargo = input("Novo cargo: ")
    novo_salario = float(input("Novo salário: "))
    novo_departamento = input("Novo departamento: ")
    return novo_cargo, novo_salario, ..