#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:20:56 2020

@author: saurabhsagar
"""

# Flask is a class of "flask"-library/framework
# so Flask contains all the prototypes that we need to build webapps from python
    # what render_template does is accesses html file stored somewhere into our pyhton file 
        # and display the html file or requested url
from flask import Flask,render_template
  
# now we create a flask object instance adn pass the flask variable
app = Flask(__name__)

# then we need a decorater route,where we will view our website
@app.route('/')

# the output this function produces will be mapped to the url given in route function given above

# all the html pages we are using here should be present in a folder name- templets

def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

# __name__ == "__main__" is used when script is executed
#  but if we import the script say script.py the condition will be like __name__ == "scrpit.py" 
if __name__ == "__main__":
    app.run(debug = True)



