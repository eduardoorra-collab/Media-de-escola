class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def transformar_em_json(self):
        return {"nome": self.nome, "nota": self.nota}