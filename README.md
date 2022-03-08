# rttag

## Introduction

This is a python web portal to manage tagging of the RT ticketing system
for faster filtering within RT

This is a first version and this software is under development.
Future versions will include other requested functionality.

## Dependencies

The code has a couple of dependencies.

### bottle

Bottle is a python light weight web framework which is only dependent on one file, 
does not need to be installed and can be downloaded using...

````
wget http://bottlepy.org/bottle.py
````

More information about bottle can be found at https://bottlepy.org/docs/dev/

### Apache

The Apache HTTP Server with **cgi-bin** More information with https://httpd.apache.org/

## Installation

Goto to your the cgi-bin folder of your apache installation

````
git clone https://github.com/menzzana/rttag
wget http://bottlepy.org/bottle.py
````

# License

cmatrix
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
