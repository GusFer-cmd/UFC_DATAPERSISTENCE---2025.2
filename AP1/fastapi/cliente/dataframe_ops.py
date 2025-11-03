import pandas as pd

alunos_df = pd.DataFrame(
    {
        "id": [1,2,3],
        "nome": ["Gustavo", "Gabriel", "Guilherme"],
        "curso": ["SI", "ADS", "AGP"],
        "nota": [9.2, 8.4, 3.2]
    }
)

print(alunos_df)
print("=====================================================")
print(alunos_df.to_dict(orient="records"))
print(alunos_df.to_dict(orient="records")[0].get("nota"))

print("======================== Filtro ======================")
print("=============== Por Id ==============")
filtroId = alunos_df["id"] == 2
print(alunos_df[filtroId])

print("=============== iloc ==============")
print(alunos_df[filtroId]["nome"].iloc[0])
print("usamos iloc para acessa a coluna desejada da linha filtrada")

print("=============== Por Nota > 7 ==============")
filtroNota = alunos_df["nota"] >= 7
print(alunos_df[filtroNota])

print("=============== Modificando elemento via iloc ==============")
a_idx = alunos_df.index[alunos_df["id"] == 2]
alunos_df.loc[a_idx, ["nota"]] = [10]
print(alunos_df)

print("=============== Apagar ==============")
a_idx = alunos_df.index[alunos_df["id"] == 1]
print(alunos_df.drop(a_idx).reset_index()) # Mantem coluna de backup
print(alunos_df.drop(a_idx).reset_index(drop=True)) # Sem coluna de backup