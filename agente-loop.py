from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True
)

while True:
    pergunta = input("Digite a sua pergunta: ")

    if pergunta.lower() in ['sair', 'exit', 'quit', 'cancelar', 'finalizar']:
        print("Encerrando agente...\nFique à vontade quando tiver mais dúvidas! 🤖")
        break

    else:
        agente.print_response(pergunta)