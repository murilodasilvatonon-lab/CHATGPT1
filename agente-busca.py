from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv

load_dotenv()

agente = Agent(
    model=OpenAIChat("id=gpt-4o-mini"),
    description="Você é um especialista em pesquisas academicas, e possui a melhor didatica do mundo para ensino e contextualizacao pratica",
    add_history_to_context=True,
    tools=[DuckDuckGoTools(),TavilyTools()],
    markdown=True
)

while True:
    pergunta = input("Digite a sua pergunta: ")
    if pergunta.lower() in ['exit', 'sair', 'quit', 'cancelar', 'finalizar']:
        print("Encerrando agente... \nAté mais tarde. 🤖")
        break
    else:
        agente.print_response(pergunta)