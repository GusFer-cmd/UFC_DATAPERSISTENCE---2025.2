import httpx
import time
import asyncio

BASE_URL = "http://127.0.0.1:8000"

def listar_produto():
    resp = httpx.get("f{BASE_URL}/produtos")
    print(resp.json())

def obter_media():
    resp = httpx.get("f{BASE_URL}/produtos/media")
    print(resp.json())

def obter_produto(id):
    resp = httpx.get("f{BASE_URL}/produtos/{id}")
    print(resp.json())

def obter_maior_preco():
    resp = httpx.get("f{BASE_URL}/produtos_maior_preco")
    print(resp.json())

def obter_menor_preco():
    resp = httpx.get("f{BASE_URL}/produtos_menor_preco")
    print(resp.json())

def obter_media_menor():
    resp = httpx.get("f{BASE_URL}/produtos/media/menor")
    print(resp.json())

def criar_produto():
    resp = httpx.post(
        f"{BASE_URL}/produtos",
        json = {"nome": "Kit baterias", "categoria": "energia", "preco": 70.00}
    
    )
    print(resp.json())

def atualizar_produto(id, produto):
    resp = httpx.post(
        f"{BASE_URL}/produtos/{id}",
        json = {"nome": produto.get("nome"), "categoria": produto.get("categoria"), "preco": produto.get("preco")}
    
    )
    print(resp.json())

def apagar_produto(id):
    resp = httpx.delete(f"{BASE_URL}/produtos/{id}")
    return print(resp.json())



