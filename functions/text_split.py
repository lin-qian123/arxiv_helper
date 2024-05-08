from langchain.text_splitter import RecursiveCharacterTextSplitter

# 拆分文本
def get_text_chunks(
    text,
    chunk_size: int = 768,
    chunk_overlap: int = 200
):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    return text_splitter.split_text(text)