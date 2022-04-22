#!/usr/bin/python
# coding=utf-8
"""
RTTag
Copyright (C) 2022  Henric Zazzi <hzazzi@kth.se>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
#-----------------------------------------------------------------------
import re
import sys
import cgi
import cgitb
import os
from bottle import template, response, request
import random
import unicodedata
import collections
import urllib
import json
#-----------------------------------------------------------------------
# Constants
#-----------------------------------------------------------------------
CREATE_TICKET="curl --key %s --cert %s -d \"content=%s\" https://minerva.nsc.liu.se/REST/1.0/ticket/new"
#-----------------------------------------------------------------------
# Functions
#-----------------------------------------------------------------------
def generateRandomString(length):
  RANDOMPASSWD="ABCDEFGHJKLMNPQRSTUVXYZabcdefghjkmnpqrstuvxyz23456789"
  passwd=""
  random.seed()
  for i in range(0,length):
    passwd=passwd+RANDOMPASSWD[random.randint(0,len(RANDOMPASSWD)-1)]
  return passwd
#-----------------------------------------------------------------------
def removeUnwantedChars(text):
  UNWANTED="\n\\\"'?;"
  for c in UNWANTED:
    text=text.replace(c,'')
  return text

#-----------------------------------------------------------------------
def isnumeric(s):
  try:
    n = int(s)
    return True
  except ValueError:
    return False
#-----------------------------------------------------------------------
def setKeywordsFromText(data,jsondata,type_array):
  text = re.sub("[\s:;,./#]+", " ", data['Text'].lower()).split(" ")
  for s1 in jsondata[type_array]:
    sa=s1.lower().split(" ")
    found=True
    idx=0
    for s2 in sa:
      if s2 not in text:
        found=False
        break
      if idx==0:
        idx=text.index(s2)
        continue
      idx=idx+1
      if text.index(s2)!=idx:
        found=False
        break
    if found:
      data['CF.{Keywords}'] += "," + str(type_array + "=" + s1)
#-----------------------------------------------------------------------
def reformatSendData(data):
  indata=""
  for key, value in data.items():
    indata += key + ": " + value + "\n"
  return urllib.quote_plus(indata)
#-----------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------
try:
  print("Content-type:text/html\r\n")
  reload(sys)
  sys.setdefaultencoding('utf-8')
  form = cgi.FieldStorage()
  fp=open('/var/www/cgi-bin/rttag/types.json')
  jsondata=json.load(fp)
  data = {}
  data['id'] = "ticket/new"
  data['Queue'] = "General"
  if not form.getvalue('id_project').startswith('('):
    data['CF.{Project}'] = form.getvalue('id_project')
  if form.getvalue('id_mail'):
    data['Requestor'] = form.getvalue('id_mail')
  if form.getvalue('id_summary'):
    data['Subject'] = form.getvalue('id_summary')
  if form.getvalue('id_description');
    data['Text'] = form.getvalue('id_description')
  data['CF.{Keywords}']=""
  if not form.getvalue('id_problem_type').startswith('('):
    data['CF.{Keywords}'] += str("problem_type=" + form.getvalue('id_problem_type'))
  if not form.getvalue('id_category_type').startswith('('):
    data['CF.{Keywords}'] += "," + str("category=" + form.getvalue('id_category_type'))
  if not form.getvalue('id_centre_resource').startswith('('):
    data['CF.{Keywords}'] += "," + str("resource=" + form.getvalue('id_centre_resource'))
  setKeywordsFromText(data,jsondata,"problem_type")
  setKeywordsFromText(data,jsondata,"centre_resource")
  setKeywordsFromText(data,jsondata,"category_type")
  setKeywordsFromText(data,jsondata,"software")
  if not data['CF.{Keywords}']:
    del data['CF.{Keywords}']
  indata = reformatSendData(data)
  output=os.popen(CREATE_TICKET % (
    "/var/www/cgi-bin/rttag/ssl/robot-key.pem",
    "/var/www/cgi-bin/rttag/ssl/robot-cert.pem",
    indata)).read()

  print(indata)
  print("-----")
  print(output)
  
  #print(template('redirect.tpl',text=output))  
  out_array=output.lower().split(" ")
  ticketn=out_array[out_array.index("ticket")+1]

except Exception as e:
  print(template('redirect.tpl',text=e))
