from flask import Flask, render_template, jsonify
import pandas as pd
import os

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,text
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, inspect, func
from flask import Flask, jsonify, render_template

app = Flask(__name__)

#################################################################################################################
##                                            Home Page                                                        ##
#################################################################################################################

@app.route('/')
def main():
    return render_template("homepage.html")