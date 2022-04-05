#!/usr/bin/python
# coding=utf-8
# Author: Henric Zazzi
#-----------------------------------------------------------------------
import sys
import cgi
import os
import json
from bottle import template
#-----------------------------------------------------------------------
def getJsonData(data,datatype):
  print_data="<select name='id_%s' id='id_%s'>" % (datatype,datatype)
  for s1 in data[datatype]:
    print_data += ("<option value='%s'>%s</option>" % (s1,s1))
  return print_data+"</select>"
#-----------------------------------------------------------------------
try:
  print("Content-type:text/html\r\n")
  reload(sys)
  sys.setdefaultencoding('utf-8')
  fp=open('/var/www/cgi-bin/rttag/types.json')
  data=json.load(fp)
  print(template('index.tpl',
    problem_type=getJsonData(data,"problem_type"),
    centre_resource=getJsonData(data,"centre_resource"),
    category_type=getJsonData(data,"category_type"),
    project=getJsonData(data,"project")
    ))

except Exception as e:
  print("ERROR: %s" % e)
