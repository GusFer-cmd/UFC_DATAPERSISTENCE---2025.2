import httpx
import time
import asyncio

BASE_URL = "http://127.0.0.1:8000"

def listar_alunos():
    resp = httpx.get(f"{BASE_URL}/listar")
    print(resp.json()) 

def criar_aluno():
    resp = httpx.post(
        f"{BASE_URL}/alunos",
        json = {"nome": "Pedro", "nota": 7.1}
    
    )
    print(resp.json()["mensagem"])
    print(resp.json()["aluno"])

def obter_aluno(nome):
    resp = httpx.get(f"{BASE_URL}/aluno/{nome}")
    print(resp.json())

criar_aluno()
listar_alunos()
obter_aluno("Gustavo")