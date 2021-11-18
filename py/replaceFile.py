#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import subprocess
import requests
import os
import sys
import time
import zipfile
import codecs

path = "./test/ch" #文件夹目录

old0="**请求报文"
new0="**调用接口**\n\
```\n\
\n\
```\n\
**参数：**\n\
```\n\
\n\
```\n"

old1="**响应报文"
new1="**返回数据：**\n\
```\n\
\n\
```\n"

def alter(file):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old0 in line:
                line=new0
            if old1 in line:
                line=new1
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

def myupper(file):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if line:
                if line[1]>='a' and line[1]<='z':
                    print('line:', line)
                    news=chr(ord(line[1])-32)
                    line = line[:1] + news + line[2:]
                    print('line:', line)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

def change():
    files= os.listdir(path) #得到文件夹下的所有文件名称
    for file in files: #遍历文件夹
         if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
            alter(path+"/"+file)

change()
# alter("交易接口.md")


