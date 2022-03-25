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
#-----------------------------------------------------------------------
# Constants
#-----------------------------------------------------------------------
CREATE_TICKET="curl --key %s --cert %s -d \"content=%s\" https://minerva.nsc.liu.se/REST/1.0/ticket/new"
SOFTWARE=['vasp','gromacs','bwa','nek5000','openfoam','veloxchem']
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
def setKeywordsFromText(data):
  text = re.sub("[\s:;,./#]+", " ", data['Text'].lower()).split(" ")
  for s1 in SOFTWARE:
    if s1 in text:
      data['CF.{Keywords}'] += "," + str("software=" + s1)
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
  data = {}
  data['id'] = "ticket/new"
  data['Queue'] = "General"
  data['CF.{Project}'] = form.getvalue('id_project')
  data['Requestor'] = form.getvalue('id_mail')
  data['Subject'] = form.getvalue('id_summary')
  data['CF.{Keywords}'] = str("problem_type=" + form.getvalue('id_problem_type'))
  data['CF.{Keywords}'] += "," + str("category=" + form.getvalue('id_category'))
  data['CF.{Keywords}'] += "," + str("resource=" + form.getvalue('id_centre_resource'))
  data['Text'] = form.getvalue('id_description')
  setKeywordsFromText(data)
  indata = reformatSendData(data)
  output=os.popen(CREATE_TICKET % (
    "/var/www/cgi-bin/rttag/ssl/robot-key.pem",
    "/var/www/cgi-bin/rttag/ssl/robot-cert.pem",
    indata)).read()
  print(template('redirect.tpl',text=output))  

except Exception as e:
  print(template('redirect.tpl',text=e))
