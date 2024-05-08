import os
import google.generativeai as genai
from openai import OpenAI


def make_prompt(query, relevant_passage):
  escaped = relevant_passage.replace("'", "").replace('"', "").replace("\n", " ")
  prompt = ("""You are a helpful and informative bot that answers questions using text from the reference passage included below. \
  Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
  However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
  strike a friendly and converstional tone. \
  If the passage is irrelevant to the answer, You can answer with your own knowledge, but it can't be irrelevant to the article. \
  If you are asked about the overall content of the document, you need to find summary sentences to summarize, and you can't focus on details.\
  You must answer the question in Chinese. \
  QUESTION: '{query}'
  PASSAGE: '{relevant_passage}'

    ANSWER:  
  """).format(query=query, relevant_passage=escaped)

  return prompt

def ask_gemini(prompt):
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    answer = model.generate_content(prompt)
    return answer.text

def ask_moonshot(prompt):
    MOONSHOT_API_KEY = os.getenv('MOONSHOT_API_KEY')
    client = OpenAI(
    api_key = MOONSHOT_API_KEY,
    base_url = "https://api.moonshot.cn/v1",
)
    answer = client.chat.completions.create(
    model = "moonshot-v1-8k",
    messages = [
        {"role": "user", "content": prompt}
    ],
    temperature = 0.3,
)
    return answer.choices[0].message.content

def ask_chatgpt(prompt):
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    client = OpenAI(
    api_key = OPENAI_API_KEY,
    base_url = "https://api.openai.com/v1",
)
    answer = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "user", "content": prompt}
    ],
    temperature = 0.3,
)
    return answer.choices[0].message.content




