import json

from aluno import Aluno

aluno1 = Aluno("Maria", 8)

print(aluno1.nome)
print(aluno1.nota)

with open("lista_alunos.json", "w") as f:
    json.dump(aluno1.transformar_em_json(), f)
    f.close()