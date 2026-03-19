from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))




# ==> this is how to write the code for 'embedding_openai_query'
# ==> As OpenAI  is paid platform, that's why this code can't be completed 
# ==> let's try same for 'google_gemini' which is totaly free   