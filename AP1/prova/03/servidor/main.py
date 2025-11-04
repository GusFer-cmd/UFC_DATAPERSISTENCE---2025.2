from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import time
import asyncio

app = FastAPI()

contador_id = 1

alunos_df = pd.DataFrame(
    {
        "id": [1],
        "nome": ["Gustavo"],
        "nota": [8.6]
    }
)

class Aluno(BaseModel):
    nome: str
    nota: float  

@app.get("/listar")
def listar_alunos():
    return alunos_df.to_dict(orient = "records")

@app.post("/alunos")
def criar_aluno(aluno: Aluno):

    global alunos_df, contador_id

    consulta = alunos_df["nome"] == aluno.nome
    if consulta.any():
        alunos_df.loc[consulta, "nota"] = aluno.nota
        return {
            "mensagem": "Nota do aluno atualizada com sucesso!",
            "aluno": alunos_df.loc[consulta].to_dict(orient="records")[0]
        }
    else:
        novo = {
            "id": contador_id,
            "nome": aluno.nome,
            "nota": aluno.nota
        }

    alunos_df = pd.concat([alunos_df, pd.DataFrame([novo])], ignore_index = True)
    contador_id = contador_id + 1

    return {
        "mensagem" : "Aluno criado com sucesso!",
        "aluno" : novo
    }

@app.get("/aluno/{nome}")
def obter_aluno(nome: str):

    consulta = alunos_df["nome"] == nome
    aluno = alunos_df[consulta] 

    if aluno.empty:
        raise HTTPException(status_code=404, detail=f"Aluno nome:{nome} não encontrado")
    return aluno.to_dict(orient="records")

