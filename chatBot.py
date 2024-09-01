import openai

key = open("apiOpenAi.txt",'r').readline().split(" ")[2]
print(key)

client = openai.OpenAI(api_key= key)

def enviarMensagem(mensagem : str):
    resposta =  client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "user" , "content" : mensagem[0]}
        ],
    )
    return resposta["choices"][0]["message"]["content"]

texto = input("Escreva aqui sua mensagem:\n")
resposta = enviarMensagem(texto)

print("ChatBot do Ph: " + resposta)
