from app.views import (
    exibir_menu,
    obter_dados_funcionario,
    exibir_funcionario,
    obter_novos_dados_funcionario,
)
from app.controllers import (
    cadastrar_funcionario,
    listar_funcionarios,
    buscar_funcionario,
    editar_funcionario,
    excluir_funcionario,
)

while True:
    exibir_menu()
    opcao = input("Opção: ")

    if opcao == "1":
        nome, cargo, salario, departamento = obter_dados_funcionario()
        cadastrar_funcionario(nome, cargo, salario, departamento)
    elif opcao == "2":
        funcionarios = listar_funcionarios()
        for funcionario in funcionarios:
            print(funcionario)
    elif opcao == "3":
        nome = input("Nome do funcionário: ")
        funcionario = buscar_funcionario(nome)
        exibir_funcionario(funcionario)
    elif opcao == "4":
        nome = input("Nome do funcionário a editar: ")
        novo_cargo, novo_salario, novo_departamento = obter_novos_dados_funcionario()
        if editar_funcionario(nome, novo_cargo, novo_salario, novo_departamento):
            print("Funcionário editado com sucesso!")
        else:
            print("Funcionário não encontrado.")
    elif opcao == "5":
        nome = input("Nome do funcionário a excluir: ")
        if excluir_funcionario(nome):
            print("Funcionário excluído com sucesso!")
        else:
            print("Funcionário não encontrado.")
    elif opcao == "6":
        break
    else:
        print("Opção inválida.")