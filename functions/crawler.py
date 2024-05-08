import os
import requests

def download_papers(arxiv_id):
    link = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    if not os.path.exists('pdf'):
        os.makedirs('pdf')
    
    response = requests.get(link)
    if response.status_code == 200:  # 检查请求是否成功
        filename = os.path.join('pdf', f'{arxiv_id}.pdf')
        with open(filename, 'wb') as f:
            f.write(response.content)
            print(f'下载成功，文件名：{filename}')
    else:
            print(f"下载失败，链接： {link}")  # 打印出下载失败的链接

