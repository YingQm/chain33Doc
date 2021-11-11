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
    #NB. Original query string below. It seems impossible to parse and
    #reproduce query strings 100% accurately so the one below is given
    #in case the reproduced version is not "correct".
    # response = requests.get('https://mapi.bityuan.com/v1/article/helps?cid=93', headers=headers, cookies=cookies)


chineseCids = ['60','271','273','274','275','276','277','280','281','282','283','284','85','82','67','116','286','285','120','121','122','123','124','125','113','114','126','211','289','296','235','72','73','74','75','76','77','78','79','86','88','95','93','94','100','99','98','97','96','218','102','105','104','108','110','115','118','134','135','266','291','101','265','268','269','137','287','293','294','295','389','396','398','399','400','402','403','404','405']
engCids = ['142', '143', '149', '151', '161', '162', '163', '164', '165', '166', '167', '168','169','170', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181','182','183','184', '156', '185', '186','187', '188', '192','193','194', '195', '196', '197', '198', '199', '200', '202', '203', '204', '205', '206', '207', '208', '191', '159', '209', '210']

backupPath = 'chain33doc-'+ time.strftime("%Y-%m-%d-%H%M%S") + '-bak' 

isPathExist = os.path.exists(backupPath)
if not isPathExist:
	os.makedirs(backupPath)
	print('create backup path:' + backupPath)
else:
	print('backup path:' + backupPath + ' is already exist')

chBackupPath = backupPath + '/ch/'
enBackupPath = backupPath + '/en/'

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

print("now start to backup chinese docs...")
for cid in chineseCids:
	rsp = getPage(cid)
	data=json.loads(rsp.text)
	title=data['title']
	print("-------" + cid + "-------")

	fileName = chBackupPath + title
	writeToFile(fileName, data)
#	time.sleep(1)

print("now start to backup english docs...")
for cid in engCids:
	rsp = getPage(cid)
	data = json.loads(rsp.text)
	title=data['title']
	print("-------" + cid + "-------")
	fileName = enBackupPath + title
	writeToFile(fileName, data)

#	time.sleep(1)
print("now you can compress the directory " + backupPath + " to backup the chain33 docs from https://chain.33.cn")

startdir = './' + backupPath
file_new = startdir + '.zip'
z = zipfile.ZipFile(file_new, 'w', zipfile.ZIP_DEFLATED)
for dirpath, dirnames, filenames in os.walk(startdir):
	fpath = dirpath.replace(startdir, '')
	fpath = fpath and fpath + os.sep or ''
	for filename in filenames:
		z.write(os.path.join(dirpath, filename), fpath + filename)
print('compress to ' + file_new +' ok')
z.close()
