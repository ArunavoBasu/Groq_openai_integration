
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="What is the capital of India and tell me the history of this",
    model="openai/gpt-oss-120b",
)
print(response.output_text)

###----------------------------------------------------------------------------------------------------

#### This is the old way of configure the Groq and openai #####

# import openai

# #Use Groq's send point
# openai.base_url = "https://api.groq.com/openai/v1"

# #Use Groq's api key
# openai.api_key = os.environ.get("GROQ_API_KEY")

# #Choose a groq supported model
# response = openai.chat.completions.create(
#     model="openai/gpt-oss-120b",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful chatbot"
#         },
#         {
#             "role": "user",
#             "content": "What is the capital of India?"
#         }
#     ]
# )

# print(response.choices[0].message.content)

