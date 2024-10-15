from flask import Flask, Blueprint, render_template, request, jsonify
import requests
from datetime import datetime, timedelta
from requests.exceptions import RequestException


weather = Blueprint('weather', __name__)

@weather.route('/weather')
def  fox():
    return render_template('weather.html')