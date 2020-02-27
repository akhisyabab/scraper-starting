from datetime import datetime
import io
import csv
import requests
from flask import Blueprint, redirect, url_for, render_template, make_response, Response
from sqlalchemy.sql import text

from project import db
from project.models.models import Records, TimeFetched
from project.utils.date import str2date, date2str

scraper_blueprint = Blueprint('scraper', __name__, template_folder='templates')


@scraper_blueprint.route('/', methods=['GET', 'POST'])
def home():
   return render_template('index.html')

@scraper_blueprint.route('/fetch', methods=['GET', 'POST'])
def fetch():
    return 'fetched'

