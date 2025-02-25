class Funcionario:
    def __init__(self, nome, cargo, salario, departamento):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.departamento = departamento

    def __str__(self):
        return f"{self.nome} - {self.cargo} - R$ {self.salario:.2f} - {self.departamento}"

    def to_dict(self):
        return {
            "nome": self.nome,
            "cargo": self.cargo,
            "salario": self.salario,
            "departamento": self.departamento,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            nome=data["nome"],
            cargo=data["cargo"],
            salario=data["salario"],
            departamento=data["departamento"],
        )