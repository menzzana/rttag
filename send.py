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
import unicodedata
import smtplib
import collections
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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
def sendMail(frommail,tomail,subject,message):
  msg=MIMEText(message.encode('utf-8'), 'plain', 'utf-8')
  msg.set_charset("utf-8")
  msg["Subject"]=subject
  msg["From"]=frommail
  msg["To"]=tomail
  msg['Content-Type'] = "text/html; charset=utf-8"
  smtpObj = smtplib.SMTP('localhost')
  smtpObj.sendmail(frommail,[tomail],msg.as_string())
#-----------------------------------------------------------------------
def sendForm(form):
  message="Username:"+str(form.getvalue('id_username'))+"\n"
  message=message+"Problem type:"+str(form.getvalue('id_problem_type'))+"\n"
  message=message+"Category:"+str(form.getvalue('id_category'))+"\n"
  message=message+"Centre resource:"+str(form.getvalue('id_centre_resource'))+"\n"
  message=message+"Project:"+str(form.getvalue('id_project'))+"\n"
  message=message+"Summary:"+str(form.getvalue('id_summary'))+"\n"
  message=message+"Description:"+str(form.getvalue('id_description'))+"\n"
  sendMail(str(form.getvalue('id_mail')),"support@pdc.kth.se",str(form.getvalue('id_summary')),"<pre>"+message+"</pre>")
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
  with open(filename, 'w') as f:
    for key, value in data.items():
      print(key + ": " + value, file=f)
  f.close()
  #output=os.popen(CREATE_TICKET % (key,cert,filename)).read()
  #os.remove(filename)
  #if "Ok" in output and "Created" in output:
  #  text="Your request has been sent"
  #else:
  #  text=output
  print(template('redirect.tpl',text=text))  

except Exception as e:
  print(template('redirect.tpl',text=e))
