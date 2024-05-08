import os
from functions import pdf_read
from functions import text_split
from functions import save_and_load
from functions import encode
import gc

# # 设置代理
# port = os.getenv('PORT')
# os.environ['HTTP_PROXY'] = f'http://localhost:{port}'
# os.environ['HTTPS_PROXY'] = f'http://localhost:{port}'

# 读取PDF

def load_pdf(file):

    file_name, extension = os.path.splitext(file)
    if extension == '.pdf':
        text = pdf_read.get_pdf_text(f'pdf/{file}')

        # 拆分文本
        chunks = text_split.get_text_chunks(text)

        # save
        embedings = encode.m3e_encode(chunks)
        save_and_load.save(chunks, embedings, file_name)

        # 释放内存
        del embedings, chunks
        gc.collect()



# query_zh = '玩具模型'
# query = google_gemini.zh_to_en(query_zh)

# idx = google_gemini.get_relevant_passage(query, loaded_em)
# passage = save_and_load.extract_text_from_pickle(file_name, idx)

# prompt = google_gemini.make_prompt(query, passage)

# answer = google_gemini.get_response(prompt)
# print(answer)
