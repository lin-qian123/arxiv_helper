# arxiv小助手，输入arxiv论文号进行知识问答

## 说明
- 本项目主要是自动下载arxiv论文进行知识问答，只需要输入arxiv论文号即可.
- 构建知识库模型用的是开源m3e-base模型，需要自行下载
- 问答模型支持openai-chatgpt, google-gemini, moonshot.

## 安装
1. 使用linux终端或者Windows中git bash执行  
```
git clone https://github.com/lin-qian123/arxiv_helper.git
```
2. 进入文件夹，安装python依赖库  
```
pip install requirements.txt
```
3. 下载m3e-base模型
```
git clone https://github.com/wangyingdong/m3e-base.git
```
## 使用
更改环境变量文件.env中的API为自己的API.    
运行main.py文件即可进行问答


