# pip install fastapi uvicorn pandas
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import time
import asyncio

# Comando para rodar
# python -m uvicorn main:app --reload

# Trabalhando sem bancos de dados 

# Inicializando API
app = FastAPI()

contador_id = 1
# alunos_df = pd.DataFrame(columns = ["id","nome","curso","IRA"])

alunos_df = pd.DataFrame(
    {
        "id": [1,2,3],
        "nome": ["Gustavo", "Gabriel", "Guilherme"],
        "curso": ["SI", "ADS", "AGP"],
        "IRA": [9.2, 8.4, 3.2]
    }
)

# Representação de Entidade
class Aluno(BaseModel):
    nome: str
    curso: str
    IRA: float      


@app.get("/listar")
def listar_alunos():
    return alunos_df.to_dict(orient = "records")

@app.post("/alunos")
def criar_aluno(aluno: Aluno):

    global alunos_df, contador_id

    novo = {
        "id": contador_id,
        "nome": aluno.nome,
        "curso": aluno.curso,
        "IRA": aluno.IRA
    }

    alunos_df = pd.concat([alunos_df, pd.DataFrame([novo])], ignore_index = True)
    contador_id = contador_id + 1

    return {
        "mensagem" : "Aluno criado com sucesso!",
        "aluno" : novo
    }

@app.get("/aluno/{id}")
def obter_aluno(id: int):

    consulta = alunos_df["id"] == id
    aluno = alunos_df[consulta] 

    if aluno.empty:
        raise HTTPException(status_code=404, detail=f"Aluno id:{id} não encontrado")
    return aluno.to_dict(orient="records")

@app.put("/aluno/{id}")
def editar_aluno(id: int, aluno: Aluno):
    global alunos_df
    aluno_antigo_idx = alunos_df.index[alunos_df["id"] == id]

    if aluno_antigo_idx.empty:
        raise HTTPException(status_code=404, detail=f"Aluno id:{id} não encontrado")
    alunos_df.loc[aluno_antigo_idx, ["nome", "curso", "IRA"]] = [aluno.nome, aluno.curso, aluno.IRA]

    return {
        "mensagem": f"Aluno {id} atualizado com sucesso!",
        "aluno": alunos_df.loc[aluno_antigo_idx].to_dict(orient="records")[0]
    }

@app.delete("/aluno/{id}")
def apagar_aluno(id: int):
    global alunos_df
    aluno_apagar_idx = alunos_df.index[alunos_df["id"] == id]

    if aluno_apagar_idx.empty:
         raise HTTPException(status_code=404, detail=f"Aluno id:{id} não encontrado") 
    alunos_df = alunos_df.drop(aluno_apagar_idx).reset_index(drop = True)
    return { "mensagem": f"Aluno {id} apagado com sucesso!"}

# Memoria interna: Trabalhando com dados em memória/arquivo, calculos grandes, ou bases de dados blocantes,
# use rotas sincronas
@app.get("/sinc")
def rota_sincrona():
    # operação blocante: Impede que o fluxo continue até o bloco ser executado
    time.sleep(2) 
    return {"tipo": "SÍNCRONA"}

# trabalhar com chamadas assincronas dentro da api/rota, exemplo,
# httpx, acessar uma base de dados de uma forma não blocante com asyncpg,
# ou simulando com  asyncio
@app.get("/assinc")
async def rota_assincrona():
    # simulando uma chamada assincrona
    await asyncio.sleep(2)
    return {"tipo": "ASSÍNCRONA"}