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
        pageSize=10
        allCount=0
        index=0
        with open('../config.json','r', encoding='UTF-8') as f:
            document=f.read()
            load_dict=json.loads(document)
            self.configObj=load_dict
        pageSize=self.configObj['pageItems']
        with open('../model/index-model.html','r', encoding='UTF-8') as f:
            indexHtml=f.read()
            indexHtml=indexHtml.replace('{-{config.logo}-}',self.configObj['logo'])
            indexHtml=indexHtml.replace('{-{config.path}-}',self.configObj['path'])
            indexHtml=indexHtml.replace('{-{config.title}-}',self.configObj['title'])
            indexHtml=indexHtml.replace('{-{config.author}-}',self.configObj['author'])
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
                nodeHtml=itemHtml.replace('{-{item.pageurl}-}',"html/"+self.configObj['list'][n]['page'])
                nodeHtml=nodeHtml.replace('{-{item.time}-}',self.configObj['list'][n]['date'])
                nodeHtml=nodeHtml.replace('{-{item.title}-}',self.configObj['list'][n]['title'])
                nodeHtml=nodeHtml.replace('{-{item.subcontent}-}',self.subArticle(self.configObj['list'][n]['page']))
                tagIndex= self.configObj['list'][n]['tag']
                if tagIndex>=0 and tagIndex <len(self.configObj['tag']):
                    tag=self.configObj['tag'][tagIndex]['name']
                    nodeHtml=nodeHtml.replace('{-{item.tag}-}',tag)
                else:
                    nodeHtml=nodeHtml.replace('{-{item.tag}-}','')   
                listview+=nodeHtml
            html=indexHtml.replace('{-<list.title>-}',listview)
            path=None
            if m==0:
                path='../index.html'
            else:
                path='../index-'+str(m)+'.html'
            with open(path,'w+', encoding='UTF-8') as f:
                f.write(html)


        
        
    def subArticle(self,path):
        html=""
        with open('../content/'+path,"r", encoding='UTF-8') as f:
            html=f.read()
            # pattern1=re.compile(r"<script[^>]*?>[\\s\\S]*?<\\/script",re.M|re.I)
            html=re.sub(r'<script[^>]*?>[\s\S]*?<\/script>', "", html)
            html=re.sub(r'<style[^>]*?>[\s\S]*?<\/style>', "", html)
            html=re.sub(r'<[^>]+>', "", html)
            html=re.sub(r'\s*|\t|\r|\n', "", html)
            # print html
        return html[0:400]
        
            
