from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from threading import Lock
import os

app = FastAPI()
lock = Lock()

ARQUIVO_CSV = "produtos.csv"

if os.path.exists(ARQUIVO_CSV):
    produtos_df = pd.read_csv(ARQUIVO_CSV)
else:
    produtos_df = pd.DataFrame(columns=["id", "nome", "categoria", "preco"])
    produtos_df.to_csv(ARQUIVO_CSV, index=False)

contador_id = 1

produtos_df = pd.DataFrame(
    {
        "id": [1],
        "nome": ["Teclado Gamer"],
        "categoria": ["Periféricos"],
        "preco": [280.00]
    }
)

class Produto(BaseModel):
    nome: str
    categoria: str
    preco: float      


@app.get("/produtos")
def listar_produtos():
    return produtos_df.to_dict(orient = "records")

@app.get("/produtos/media")
def obter_produto_media():

    if produtos_df.empty:
        raise HTTPException(status_code=404, detail=f"Nenhum produto encontrado")

    consulta = produtos_df["preco"].mean()

    return {"media:": consulta }

@app.get("/produtos/{id}")
def obter_produto(id: int):

    consulta = produtos_df["id"] == id
    produto = produtos_df[consulta]

    if produto.empty:
        raise HTTPException(status_code=404, detail=f"Produto id:{id} não encontrado")
    return produto.to_dict(orient="records")

@app.get("/produtos_maior_preco")
def obter_produto_maior_preco():

    if produtos_df.empty:
        raise HTTPException(status_code=404, detail=f"Nenhum produto encontrado")

    consulta = produtos_df["preco"].idxmax()
    produto = produtos_df.loc[consulta]

    return produto.to_dict()

@app.get("/produtos_menor_preco")
def obter_produto_menor_preco():

    if produtos_df.empty:
        raise HTTPException(status_code=404, detail=f"Nenhum produto encontrado")

    consulta = produtos_df["preco"].idxmin()
    produto = produtos_df.loc[consulta]

    return produto.to_dict()

@app.get("/produtos/media/maior")
def obter_produto_media_maior():

    if produtos_df.empty:
        raise HTTPException(status_code=404, detail=f"Nenhum produto encontrado")

    consulta = produtos_df["preco"].mean()
    produto_acima = produtos_df[produtos_df["preco"] >= consulta]

    return produto_acima.to_dict()

@app.get("/produtos/media/menor")
def obter_produto_media_menor():

    if produtos_df.empty:
        raise HTTPException(status_code=404, detail=f"Nenhum produto encontrado")

    consulta = produtos_df["preco"].mean()
    produto_abaixo = produtos_df[produtos_df["preco"] < consulta]

    return produto_abaixo.to_dict()

@app.post("/produtos")
def criar_produto(produto: Produto):
    
    global produtos_df, contador_id

    with lock: 
        novo = {
            "id": contador_id,
            "nome": produto.nome,
            "categoria": produto.categoria,
            "preco": produto.preco
        }

    produtos_df = pd.concat([produtos_df, pd.DataFrame([novo])], ignore_index = True)
    contador_id = contador_id + 1

    produtos_df.to_csv(ARQUIVO_CSV, index=False)

    return {
        "mensagem" : "Produto criado com sucesso!",
        "produto" : novo
    }

@app.put("/produtos/{id}")
def atualizar_produto(id: int, produto: Produto):
    global produtos_df
    
    with lock: 
        antigo_produto_idx = produtos_df.index[produtos_df["id"] == id]

    if antigo_produto_idx.empty:
        raise HTTPException(status_code=404, detail=f"Produto id:{id} não encontrado")
    produtos_df.loc[antigo_produto_idx, ["nome", "categoria", "preco"]] = [produto.nome, produto.categoria, produto.preco]

    produtos_df.to_csv(ARQUIVO_CSV, index=False)

    return {
        "mensagem" : "Produto atualizado com sucesso!",
        "produto" : produtos_df.loc[antigo_produto_idx].to_dict(orient="records")[0]
    }

@app.delete("/produtos/{id}")
def deletar_produto(id: int):
    global produtos_df
    with lock: 
        antigo_produto_idx = produtos_df.index[produtos_df["id"] == id]

    if antigo_produto_idx.empty:
         raise HTTPException(status_code=404, detail=f"Aluno id:{id} não encontrado") 
    produtos_df = produtos_df.drop(antigo_produto_idx).reset_index(drop = True)

    produtos_df.to_csv(ARQUIVO_CSV, index=False)

    return { "mensagem": f"Produto {id} apagado com sucesso!"}