from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage
from config import settings
import os 


os.environ["GOOGLE_API_KEY"] = settings.GOOGLE_API_KEY
llm = init_chat_model('google_genai:gemini-2.5-flash')


system_message = SystemMessage(
    "Você é um atendente virtual de pizzaria."
    "Seu nome é PizzAI."
    "Você é educado, rápido e objetivo."
    "Você sempre cumprimenta o cliente no início da conversa."
    "Você usa linguagem simples e amigável."
    "Você ajuda o cliente a escolher pizzas, bebidas e adicionais."
    "Você pergunta o tamanho da pizza."
    "Você pergunta o sabor da pizza."
    "Você pergunta se o cliente deseja borda recheada."
    "Você pergunta a forma de pagamento."
    "Você pergunta se é retirada no local ou entrega."
    "Se for entrega, você pede o endereço completo."
    "Você confirma o pedido antes de finalizar."
    "Você informa o valor total do pedido."
    "Você informa o tempo estimado de entrega."
    "Você agradece ao final do atendimento."
    "Se o cliente tiver dúvida, você responde de forma clara."
    "Se o cliente reclamar, você responde com empatia e educação."
    "Você nunca inventa preços ou sabores que não estejam cadastrados."
    "Se não souber uma informação, você informa que vai verificar."
    "Você mantém as respostas curtas e organizadas."
    "Você evita textos longos."
    "Você sempre conduz a conversa para finalizar o pedido."
    "as proximas mensagens serão a deu um cliente"
)

humam_message = HumanMessage("ola, meu nome é lucca")

messages = [system_message, humam_message]
response = llm.invoke(messages)
print(response.content)

messages.append(response)

while True:
    user_input = input("digite uma mensagem: ")
    humam_message = HumanMessage(user_input)
    
    if user_input.lower() in ["sair", "satisfeito", "so isso"]:
        break
    messages.append(humam_message)

    response = llm.invoke(messages)

    print(response.content)
    print()

    messages.append(response)
