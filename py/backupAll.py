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

fileNamepath = "./from.html"
chineseCids = []
engCids = []
backupPath = 'chain33doc-'+ time.strftime("%Y-%m-%d-%H%M%S") + '-bak'
chBackupPath = backupPath + '/ch/'
enBackupPath = backupPath + '/en/'

def getId():
    en=0
    with open(fileNamepath, "r", encoding="utf-8") as f:
        for line in f:
            if "data-key" in line and "treegrid-parent" in line:
                if "treegrid-expanded" in line:
                    continue
                else:
                    findKey=line.find("data-key=")+len("data-key=")+1
                    id=line[findKey:findKey+3]
                    if "\"" in id:
                        id=id[0:2]
                    if id == "148" or id == "144":
                        en=1
                    if en == 0:
                        chineseCids.append(id)
                    else:
                        engCids.append(id)
    print("chineseCids:",chineseCids)
    print("engCids:",engCids)

def writeToFile(fileName, data):
    fileName = fileName + ".md"
    file = codecs.open(fileName, 'w', 'utf-8')
    file.write(data['body'])
    file.close()

def getPage(cid):
    cookies = {
        'UM_distinctid': '16bd01c24457a4-0b0d5ed29524ae-19251202-1fa400-16bd01c244690a',
    }

    headers = {
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    params = (
        ('cid', cid),
    )

    response = requests.get('https://mapi.bityuan.com/v1/article/helps', headers=headers, params=params, cookies=cookies)
    return response



def writeToFileCid(cids, backupPath):
    for cid in cids:
        rsp = getPage(cid)
        data=json.loads(rsp.text)
        title=data['title']
        print("-------" + cid + "-------")
        fileName = backupPath + title
        writeToFile(fileName, data)


def initBackupPath():
    isPathExist = os.path.exists(backupPath)
    if not isPathExist:
        os.makedirs(backupPath)
        print('create backup path:' + backupPath)
    else:
        print('backup path:' + backupPath + ' is already exist')

    isPathExist = os.path.exists(chBackupPath)
    if not isPathExist:
        os.makedirs(chBackupPath)
        print('create chinese backup path:' + chBackupPath)
    else:
        print('chinese backup path:' + chBackupPath + ' is already exist')

    isPathExist = os.path.exists(enBackupPath)
    if not isPathExist:
        os.makedirs(enBackupPath)
        print('create english backup path:' + enBackupPath)
    else:
        print('english backup path:' + enBackupPath + ' is already exist')


# print("now start to backup chinese docs...")

# initBackupPath()
getId()
# writeToFileCid(chineseCids,chBackupPath)
# writeToFileCid(engCids,enBackupPath)

# print("now you can compress the directory " + backupPath + " to backup the chain33 docs from https://chain.33.cn")


