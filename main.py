import json
from openai import OpenAI
from dotenv import load_dotenv
from tools import data_atual, calcular_imc, gerar_senha
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

historico_mensagens = []


def salvar_json():
    with open("memoria.json", "w", encoding="utf-8") as f:
        json.dump(historico_mensagens, f, indent=2, ensure_ascii=False)


def carregar_json():
    global historico_mensagens

    try:
        with open("memoria.json", "r", encoding="utf-8") as f:
            historico_mensagens = json.load(f)
    except:
        pass


carregar_json()

if not historico_mensagens:
    historico_mensagens.append({
        "role": "system",
        "content": "Você é um assistente educado, objetivo e levemente bem-humorado. "
                   "Responda de forma clara e útil."
    })

def salvar_historico(mensagem):
    historico_mensagens.append(mensagem)

    LIMITE = 10

    if len(historico_mensagens) > LIMITE:
        historico_mensagens.pop(1)  
        
    salvar_json()

def chat(pergunta):
    salvar_historico({"role": "user", "content": pergunta})

    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=historico_mensagens
    )

    resposta_conteudo = resposta.choices[0].message.content
    salvar_historico({"role": "assistant", "content": resposta_conteudo})
    return resposta_conteudo

def salvar_json():
    with open("memoria.json", "w", encoding="utf-8") as f:
        json.dump(historico_mensagens, f, indent=2, ensure_ascii=False)
        
def carregar_json():
    global historico_mensagens

    try:
        with open("memoria.json", "r", encoding="utf-8") as f:
            historico_mensagens = json.load(f)
    except:
        pass

while True:
    pergunta = input("Você: ")
    
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Encerrando o chat. Até mais!")
        break

    if pergunta.lower() == "/limpar":
        historico_mensagens.clear()

        historico_mensagens.append({
            "role": "system",
            "content": "Você é um assistente educado, objetivo e levemente bem-humorado."
        })

        print("Assistente: Memória da conversa apagada.")
        continue

    if "data" in pergunta.lower():
        salvar_historico({"role": "user", "content": pergunta})
        resposta = "Hoje é " + str(data_atual())
        salvar_historico({"role": "assistant", "content": resposta})
        print("Assistente: " + resposta)
        continue
    
    if "imc" in pergunta.lower():

        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))

        imc = calcular_imc(peso, altura)

        resposta = f"Seu IMC é {imc:.2f}"

        salvar_historico({"role": "assistant", "content": resposta})
        print("Assistente:", resposta)
        continue
    
    if "senha" in pergunta.lower():

        senha = gerar_senha()

        resposta = f"Sua senha gerada é: {senha}"

        salvar_historico({"role": "assistant", "content": resposta})
        print("Assistente:", resposta)
        continue

    resposta = chat(pergunta)
    print("Assistente: ", resposta)
