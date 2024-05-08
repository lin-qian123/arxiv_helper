from sentence_transformers import SentenceTransformer
import numpy as np

def m3e_encode(chunks):
    model = SentenceTransformer('embeding_model/m3e-base')
    embedings = model.encode(chunks)
    return embedings

def get_relevant_passage(query, embedings):
    model = SentenceTransformer('embeding_model/m3e-base')
    query_embedding = model.encode(query)
    dot_products = np.dot(np.stack(embedings), query_embedding)
    sorted_indices = np.argsort(-dot_products)
    idx = sorted_indices[:10]
    return idx