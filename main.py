quantidade_alunos = int(input("Digite a quantidade de alunos:"))
  

for numero_aluno in range(1, quantidade_alunos + 1):
        print("Digite a nota do aluno", numero_aluno)
        nota = float(input())
        if nota >= 7:
            print("Aprovado")
        elif nota >= 5:
            print("Recuperação")
        else:
            print("Reprovado")