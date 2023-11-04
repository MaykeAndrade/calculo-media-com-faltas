aluno = input("Digite o nome do aluno(a): ")
media = float(input("Digite a media do aluno(a): "))
faltas = int(input("  Digite o numero de faltas do aluno(a): "))

if media >= 7 and faltas < 10:
    resultado = ("Aprovado")
elif media < 7 and faltas < 10:
    resultado = ("Reprovado por media")
elif faltas >= 10:
    resultado = ("Reprovado por faltas")
else media < 7 and faltas >= 10:
    resultado = ("Reprovado por media e faltas")

print(f"O aluno(a) {aluno} teve media {media} e faltas {faltas} e o resultado foi {resultado}")