from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

def generate_kid_name(kid_type, kid_country):
    #1. create model
    model = ChatOpenAI(temperature=0.7)
    #2. create parser
    parser = StrOutputParser()
    #3. Create prompt template
    prompt_template_name = ChatPromptTemplate([
            ('user', "I have a {kid_country} {kid_type} and I want a name. Suggest me five names for my kid")
            ])
    name_chain = prompt_template_name | model | parser

    response = name_chain.invoke({'kid_type' : kid_type, 'kid_country':kid_country})

    return response

