from langchain_openai import ChatOpenAI
import os

os.environ['OPENAI_API_KEY'] = "lick my balls openAi"

gemma2 = ChatOpenAI(
  model='ollama/gemma:2b',
  base_url="http://localhost:11434"
)
