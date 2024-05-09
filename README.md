# arxiv小助手，输入arxiv论文号进行知识问答

## 说明
- 本项目主要是自动下载arxiv论文构建知识库进行问答，只需要输入arxiv论文号即可.
- 构建知识库模型用的是开源文本转向量m3e-base模型，需要额外下载.
- 问答模型支持openai-chatgpt, google-gemini, moonshot.

## 安装
1.使用linux终端或者Windows中git bash执行  
```
git clone https://github.com/lin-qian123/arxiv_helper.git
```
或者直接下载zip压缩包.

2.进入文件夹，安装python依赖库  
```
pip install requirements.txt
```
3.下载m3e-base模型
```
git clone https://github.com/wangyingdong/m3e-base.git
```
## 使用
更改环境变量文件.env中的API为自己的API.    
运行main.py文件即可进行问答.

## 基本思路
首先下载PDF并且将其拆分成文本，然后将文本块embeding成相应向量，在每次输入问题时，将问题对应的向量与文本向量作内积，提取出相似度最高的文本进行问答。



