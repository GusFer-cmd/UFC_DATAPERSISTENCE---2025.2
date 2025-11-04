with open("./dados_alunos.txt", "r") as file:
    
    total = 0
    contador = 0
    nota_maior = -1
    nota_menor = 11
    maior = ""
    menor = ""
 
    for linha in file:
        valores = linha.strip().split('#')
        nome = valores[0]
        curso = valores[1]
        nota = float(valores[2])

        total = total + nota
        contador = contador + 1

        if nota > nota_maior:
            nota_maior = nota
            maior = nome

        elif nota < nota_menor:
            nota_menor = nota
            menor = nome

    media = total/contador

    print(f"Media da turma: {media}")
    print(f"Maior nota: {nota_maior} - Aluno: {maior}")
    print(f"Menor nota: {nota_menor} - Aluno: {menor}")
    