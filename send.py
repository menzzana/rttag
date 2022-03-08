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
import os
from bottle import template, response, request
#-----------------------------------------------------------------------
# Constants
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Functions
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
  reload(sys)
  sys.setdefaultencoding('utf8')
  form = cgi.FieldStorage()
  response.content_type = 'text/html; charset=UTF-8' 
  print(response)
  
  if username is None:
    print(template('redirect.tpl',link="index.py",text="Wrong username/password"))
    exit(0)
  if form.getvalue('page')=="add_competence":
    user_id=getID(cur,"user","username",username)
    category_id=getID(cur,"category","id",form.getvalue('category_id'))
    competence_id=getID(cur,"competence","name",form.getvalue('mycompetence'))
    if competence_id is None:
      cur.execute(NEWCOMPETENCE,(category_id,form.getvalue('mycompetence')))
      competence_id=getID(cur,"competence","name",form.getvalue('mycompetence'))
    cur.execute(CHECKUSERCOMPETENCE,(user_id,competence_id))
    row=cur.fetchone()
    if row is None:
      cur.execute(INSERTUSERCOMPETENCE,(user_id,competence_id,form.getvalue('scale_id')))
      text="New user competence has been added"
    else:
      cur.execute(UPDATEUSERCOMPETENCE,(form.getvalue('scale_id'),row[0]))
      text="User competence has been updated"
  if form.getvalue('page')=="pers_cmatrix":
    for key in form.keys():
      value=form.getvalue(key)
      if key=='page' or value=="0":
        continue
      # In python3 convert to key.isnumeric()
      if isnumeric(key):
        cur.execute(UPDATEUSERCOMPETENCE,(value,key))
      else:
        competence_id=getID(cur,"competence","name",key)
        user_id=getID(cur,"user","username",username)
        cur.execute(INSERTUSERCOMPETENCE,(user_id,competence_id,value))
    text="User competence has been updated"

  print(template('redirect.tpl',link=form.getvalue('page')+".py",text=text))  

except Exception as e:
  print(template('redirect.tpl',link="add_competence.py",text=e))
