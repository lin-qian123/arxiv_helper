import os
from functions import crawler
import load
from functions import save_and_load
import ask

# # 设置代理
# port = os.getenv('PORT')
# os.environ['HTTP_PROXY'] = f'http://localhost:{port}'
# os.environ['HTTPS_PROXY'] = f'http://localhost:{port}'

## 选择模型
model = input("请选择模型，选择前确保在.env文件配置正确的api_key（输入1、2或3）：\n1. ChatGPT\n2. Moonshot\n3. Gemini\n")
## 下载并加载论文
paper_id = input("请输入arxiv论文号：")
if os.path.exists('vec_data/' + paper_id + '.npy'):
    print("文件已存在，直接加载知识库...")
    loaded_em = save_and_load.load_vec(paper_id)
    print("加载成功，现在可以提问啦！注意，小助手回答没有记忆。请输入你的问题（或输入'退出'来结束）：")
else:
    print("文件不存在，正在下载论文...")
    crawler.download_papers(paper_id)
    print('正在加载知识库...（可能需要较长时间，取决于电脑配置）')
    
    try:
        load.load_pdf(paper_id + '.pdf')
        loaded_em = save_and_load.load_vec(paper_id)
        print("加载成功，现在可以提问啦！注意，小助手回答没有记忆。请输入你的问题（或输入'退出'来结束）：")
    except Exception as e:
        print("加载失败，请检查原因")
        print(str(e))

while True:
    question = input("你：")
    if question.lower() == '退出':
        break
    if model == '1':
        answer = ask.ask_question_chatgpt(question, loaded_em, paper_id)
    elif model == '2':
        answer = ask.ask_question_moonshot(question, loaded_em, paper_id)
    elif model == '3':
        answer = ask.ask_question_gemini(question, loaded_em, paper_id)
    print("小助手：", answer)

# # 创建 Gradio 界面
# gr.Interface(download_papers_with_input, 
#               inputs="text",
#               outputs="text",
#               title="下载论文",
#               description="输入URL并点击提交按钮以下载论文，右侧将显示PDF文件夹中的文件名称。",
#               allow_flagging=False # 禁用标记功能，因为我们没有输出组件
#              ).launch(share=True)

