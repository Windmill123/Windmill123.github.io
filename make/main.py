#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import re
import json
import copy
import string
from CreateHtml import BlogHtml
from CreateItemHtml import ItemHtml
# defaultencoding = 'utf-8'
# if sys.getdefaultencoding() != defaultencoding:
#     reload(sys)
#     sys.setdefaultencoding(defaultencoding)
page=ItemHtml()
page.createHtml()
blog=BlogHtml()
blog.create_index()
# print("123")