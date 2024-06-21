alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

aprovados = [aluno for i, aluno in enumerate(alunos) if notas[i] >= 60]
print("Aprovados:", aprovados)