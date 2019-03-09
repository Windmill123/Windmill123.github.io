#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import re
import json
import copy
import string
import os
import os.path
class ItemHtml:
    configObj=None
    htmlModel=None
    def __init__(self):
        with open('../config.json','r', encoding='UTF-8') as f:
            document=f.read()
            load_dict = json.loads(document)
            self.configObj=load_dict
    def createHtml(self):
        with open('../model/content-model.html','r', encoding='UTF-8') as f:
            self.htmlModel=f.read()
        if self.configObj and self.createHtml:
            self.htmlModel=self.htmlModel.replace("{-{config.logo}-}",self.configObj["logo"])
            self.htmlModel=self.htmlModel.replace("{-{config.author}-}",self.configObj["author"])
            self.htmlModel=self.htmlModel.replace("{-{config.title}-}",self.configObj['title'])
        for obj in self.configObj["list"]:
            # print obj
            html=""
            sourceHtml=copy.deepcopy(self.htmlModel)
            sourceHtml=sourceHtml.replace("{-{page.path}-}","../")
            sourceHtml=sourceHtml.replace("{-{index.itemPage.title}-}",obj["title"])
            sourceHtml=sourceHtml.replace("{-{index.itemPage.time}-}",obj["date"])
            if obj["isCreate"]:
                with open("../content/"+obj["page"],"r", encoding='UTF-8') as target:
                    html=target.read()
                with open("../html/"+obj["page"],"w+", encoding='UTF-8') as fi:
                    sourceHtml=sourceHtml.replace("{-(html.index.itemPage)-}",html)
                    fi.write(sourceHtml)