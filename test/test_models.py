import unittest
from app.models import Funcionario

class TestFuncionario(unittest.TestCase):
    def test_funcionario_creation(self):
        funcionario = Funcionario("João", "Desenvolvedor", 5000.0, "TI")
        self.assertEqual(funcionario.nome, "João")
        self.assertEqual(funcionario.cargo, "Desenvolvedor")
        self.assertEqual(funcionario.salario, 5000.0)
        self.assertEqual(funcionario.departamento, "TI")

    def test_funcionario_str(self):
        funcionario = Funcionario("Maria", "Gerente", 8000.0, "Administração")
        self.assertEqual(str(funcionario), "Maria - Gerente - R$ 8000.00 - Administração")

    def test_funcionario_to_dict(self):
        funcionario = Funcionario("Carlos", "Analista", 6000.0, "RH")
        funcionario_dict = funcionario.to_dict()
        self.assertEqual(funcionario_dict["nome"], "Carlos")

    def test_funcionario_from_dict(self):
        funcionario_dict = {"nome": "Ana", "cargo": "Designer", "salario": 4500.0, "departamento": "Marketing"}
        funcionario = Funcionario.from_dict(funcionario_dict)
        self.assertEqual(funcionario.nome, "Ana")

if __name__ == '__main__':
    unittest.main()