from flask import Blueprint, render_template
import requests

frontend = Blueprint('frontend', __name__)
@frontend.route('/frontend/fixtures/<int:date>')
def bydate(date):
    datas = requests.get('http://localhost:5000/schedule/bydate/{date}'.format(date=date))
    data = datas.json()
    return render_template('fixture-grid.html',data=data)

@frontend.route('/frontend/fixtures')
def todays_game():
    datas = requests.get('http://localhost:5000/schedule/todays_game')
    data = datas.json()
    return render_template('fixture-grid.html',data=data)