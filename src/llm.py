from langchain_openai import ChatOpenAI

llama2 = ChatOpenAI(
  model='ollama/gemma:2b',
  base_url="http://localhost:11434"
)
