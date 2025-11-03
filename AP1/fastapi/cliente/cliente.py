# pip install httpx
import httpx
import time
import asyncio

BASE_URL = "http://127.0.0.1:8000"

def criar_aluno():
    resp = httpx.post(
        f"{BASE_URL}/alunos",
        json = {"nome": "Fernandes", "curso": "SI", "IRA": 7.1}
    
    )
    print(resp.json()["mensagem"])
    print(resp.json()["aluno"])


def listar_alunos():
    resp = httpx.get(f"{BASE_URL}/alunos")
    print(resp.json()) 

def obter_aluno(id):
    resp = httpx.get(f"{BASE_URL}/aluno/{id}")
    print(resp.json())

def atualizar_aluno(id, aluno):
    resp = httpx.put(
        f"{BASE_URL}/aluno/{id}",
        json = {"nome": aluno.get("nome"), "curso": aluno.get("curso"), "IRA": aluno.get("IRA")}
    )
    return resp.json()

def apagar_aluno(id):
    resp = httpx.delete(f"{BASE_URL}/aluno/{id}")
    return print(resp.json())

def chamar_rota():

    inicio = time.time()

    resp_sinc = httpx.get(f"{BASE_URL}/sinc")
    print(resp_sinc.json())

    resp_assinc = httpx.get(f"{BASE_URL}/assinc")
    print(resp_assinc.json())

    fim = time.time()
    print(f"Tempo total: {fim - inicio:.2f} segundos")

async def chamar_rota_assinc():

    inicio = time.time()

    async with httpx.AsyncClient() as client:
        r1, r2 = await asyncio.gather(
            client.get(f"{BASE_URL}/assinc"),
            client.get(f"{BASE_URL}/sinc"),
        )
        print("R1: ", r1.json())
        print("R2: ", r2.json())

    fim = time.time()
    print(f"Tempo total: {fim - inicio:.2f} segundos")


# criar_aluno()
# listar_alunos()
# obter_aluno(2)
# print(obter_aluno(2).get("nota"))
# atualizar_aluno(1, {"nome": "Midorya", "curso": "Hero", "IRA": 10})
# chamar_rota()
# asyncio.run(chamar_rota_assinc())
