import os
from functions import save_and_load
from functions import encode
from llm import llm


def ask_question_chatgpt(query, loaded_em, file_name):

    idx = encode.get_relevant_passage(query, loaded_em)
    passage = save_and_load.extract_text_from_pickle(file_name, idx)
    prompt = llm.make_prompt(query, passage)
    answer = llm.ask_chatgpt(prompt)
    return answer

def ask_question_moonshot(query, loaded_em, file_name):

    idx = encode.get_relevant_passage(query, loaded_em)
    passage = save_and_load.extract_text_from_pickle(file_name, idx)
    prompt = llm.make_prompt(query, passage)
    answer = llm.ask_moonshot(prompt)
    return answer

def ask_question_chatgpt(query, loaded_em, file_name):

    idx = encode.get_relevant_passage(query, loaded_em)
    passage = save_and_load.extract_text_from_pickle(file_name, idx)
    prompt = llm.make_prompt(query, passage)
    answer = llm.ask_gemini(prompt)
    return answer



