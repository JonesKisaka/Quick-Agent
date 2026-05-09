from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(model="claude-opus-4-6")
llm2 = ChatOpenAI(model="gpt-4o-mini")

response = llm.invoke("What is the meaning of life?")
print (response)