from dotenv import load_dotenv
from agno.agent  import Agent 
from agno.models.openai import OpenAIChat

pergunta =input("Faça uma pergunta: ")

#Todos os agentes necessitam da chave de API, a função LOAD_DOTENV faz a leitura do arquivo no .env.
load_dotenv()

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True
)

agente.print_response(pergunta)