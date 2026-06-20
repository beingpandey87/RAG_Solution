import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv('OPENAI_API_KEY'))
from langchain_core import __version__ as langchain_core_version
#from langgraph import __version__ as lg_version

#display versions of langchain and langgrain
print(f"Langchain version: {langchain_core_version}")
#print(f"Langgrain version: {lg_version}")

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

def main():
    #test OpenAI
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    response = llm.invoke("Say setup complete in one sentence.")
    print(response)

if __name__ == "__main__":
    main()