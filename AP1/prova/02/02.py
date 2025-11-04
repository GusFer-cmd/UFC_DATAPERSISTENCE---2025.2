import pandas as pd

notas = pd.Series([12000, 17500, 14300, 16000, 16000],
    index = ["Luca Brasi","Peter Clemenza","Sal Tessio","Tom Hagen", "Michael Corleone"])

somatoria = notas.sum()
print("Total arrecadado na semana:")
print(somatoria)

print("====================================")

media = notas.mean()
print("Media das receitas:")
print(media)

print("====================================")

acima = notas[notas > notas.mean()]
print("Acima da media:")
print(acima)

print("====================================")
