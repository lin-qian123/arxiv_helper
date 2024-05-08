import numpy as np
import pickle

def save(chunks, embedings, name):
    np.save(f'vec_data/{name}.npy', embedings)
    with open(f'vec_data/{name}.pkl', 'wb') as f:
        pickle.dump(chunks, f)

def load_vec(name):
    loaded_vec = np.load(f'vec_data/{name}.npy')
    return loaded_vec

def extract_text_from_pickle(name, indices):
    extracted_text = []
    # 加载.pkl文件
    with open(f'vec_data/{name}.pkl', 'rb') as f:
        text_list = pickle.load(f)
        # 根据索引提取相应的文本
        for idx in indices:
            extracted_text.append(text_list[idx])
    # 将提取的文本连接成一个文本
    return ' '.join(extracted_text)




