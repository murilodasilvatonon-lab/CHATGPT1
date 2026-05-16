from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um especialista em pesquisas acadêmicas e possui a melhor didática do mundo para ensino e contextualização prática",
    tools=[DuckDuckGoTools()],
    markdown=True
)

while True:
    pergunta = input("Digite a sua pergunta: ")

    if pergunta.lower() in ['sair', 'exit', 'quit', 'cancelar', 'finalizar']:
        print("Encerrando agente...\nFique à vontade quando tiver mais dúvidas! 🤖")
        break

    else:
        agente.print_response(pergunta)