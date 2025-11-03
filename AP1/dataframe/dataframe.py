# Viavel porem necessita mexer no objeto pilotos para alterções futuras
import pandas as pd

# pilotos = {
#     'Nome': ['Ayrton Senna', 'Alain Prost', 'Rubens Barrichello'],
#     'Nacionalidade': ['Brasileiro', 'Frances', 'Brasileiro'],
#     'Numero de Titulos': [3, 4, 0]
# }

# pilots_df = pd.DataFrame(pilotos)
# print(pilots_df)


########################################


# Para um unico piloto
pilotos_v2 = {
    'nome': "Charles LeClerc",
    'nacionalidade': 'monegasto',
    'titulos': 0,
}

piloto_df = pd.DataFrame([pilotos_v2])

########################################


# persistindo na base de dados
pilotos_csv = pd.read_csv('./pilotos.csv')

# concatenar
pilotos_csv = pd.concat([pilotos_csv, piloto_df], ignore_index= True)
# print(pilotos_csv)
# pilotos_csv.to_csv("pilotos.csv", index = False)

# usando append
# pilotos_csv = pilotos_csv._append(pilotos_v2, ignore_index = True)