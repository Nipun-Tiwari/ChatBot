# langchain_agent.py
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import requests

# Define a prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="Answer the following question: {question}"
)

# Initialize LLM (e.g., OpenAI GPT-3)
llm = OpenAI(api_key="your_openai_api_key")

# Create a chain
chain = LLMChain(llm=llm, prompt=prompt)

def query_backend(question: str):
    # Send the question to the FastAPI backend
    response = requests.get(f"http://127.0.0.1:8000/query?question={question}")
    return response.json()

def get_response(question: str):
    # Use LangChain to refine the question or generate a response
    refined_question = chain.run(question)
    backend_response = query_backend(refined_question)
    return backend_response["response"]