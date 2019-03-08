#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import re
import json
import copy
import string
class BlogHtml:
    catePath=""
    configObj=None
    def __init__(self):
        pass
    def create_index(self):
        document=None
        load_dict=None
        indexHtml=None
        itemHtml=None
        pageCount=0
        pageSize=3
        allCount=0
        index=0
        with open('../config.json','r', encoding='UTF-8') as f:
            document=f.read()
            load_dict=json.loads(document)
            self.configObj=load_dict
        with open('../model/index-model.html','r', encoding='UTF-8') as f:
            indexHtml=f.read()
            # print(indexHtml)
        with open('../model/index-item-model.html','r', encoding='UTF-8') as f:
            itemHtml=f.read()
        allCount=len(self.configObj['list'])
        if allCount%pageSize==0 :
            pageCount=int(allCount/pageSize)
        else :
            pageCount=int(allCount/pageSize)+1
        print('page count=   '+str(pageCount))
        for m in range(0,pageCount):
            listview=''
            html=''
            a=m*pageSize
            b=(m+1)*pageSize
            if m>=(pageCount-1):
                b=allCount
            for n in range(a,b):
                nodeHtml=itemHtml.replace('{123}',self.configObj['list'][n]['date'])
                listview+=nodeHtml
            html=indexHtml.replace('<-<node.pagelist>->',listview)
            path=None
            if m==0:
                path='../index.html'
            else:
                path='../index-'+str(m)+'.html'
            with open(path,'w+', encoding='UTF-8') as f:
                f.write(html)


        
        
        # for obj in self.configObj['list']:
        #     pass
        
            
