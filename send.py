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
import sys
import cgi
import cgitb
import os
from bottle import template, response, request
import random
import unicodedata
import collections
#-----------------------------------------------------------------------
# Constants
#-----------------------------------------------------------------------
CREATE_TICKET="curl --key %s --cert %s --data-urlencode content@%s https://minerva.nsc.liu.se/REST/1.0/ticket/new"
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
# Main
#-----------------------------------------------------------------------
try:
  print("Content-type:text/html\r\n")
  reload(sys)
  sys.setdefaultencoding('utf-8')
  form = cgi.FieldStorage()
  filename = str(generateRandomString(10))+".txt"
  data = {}
  data['id'] = "ticket/new"
  data['Queue'] = "General"
  data['Requestor'] = form.getvalue('id_mail')
  data['Subject'] = form.getvalue('id_summary')
  data['CF.{Keywords}'] = str(form.getvalue('id_problem_type'))
  data['CF.{Keywords}'] += "," + str(form.getvalue('id_category'))
  data['CF.{Keywords}'] += "," + str(form.getvalue('id_centre_resource'))
  data['Text'] = form.getvalue('id_description')
  fp = open(filename, "w")
  for key, value in data.items():
    fp.write(key + ": " + value + "\n")
  fp.close()
  output=os.popen(CREATE_TICKET % ("ssl/robot-key.pem","ssl/robot-cert.pem",filename)).read()
  os.remove(filename)
  print(template('redirect.tpl',text=output))  

except Exception as e:
  print(template('redirect.tpl',text=e))
