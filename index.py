#!/usr/bin/python
# coding=utf-8
# Author: Henric Zazzi
#-----------------------------------------------------------------------
import sys
import cgi
import os
from bottle import template
#-----------------------------------------------------------------------
try:
  print("Content-type:text/html\r\n")
  reload(sys)
  sys.setdefaultencoding('utf-8')
  print(template('index.tpl'))

except Exception as e:
  print("ERROR: %s" % e)
